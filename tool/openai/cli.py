import os
import sys
import time
import argparse
from datetime import datetime, timedelta
from openai import OpenAI
from dotenv import load_dotenv

# Usage: script
# ENV=.env
# DIR=snippet/tool/openai
# $DIR/.venv/bin/python $DIR/cli.py -e $ENV $@

def format_batch(batch):
	msg = "=" * 40 + "\n"
	msg += f"id: {batch['id']} | status: {batch['status']}\n"

	# Time
	msg += f"T: {datetime.fromtimestamp(batch['created_at']).strftime("%Y-%m-%d | %H:%M:%S")} ~"
	if batch['completed_at']:
		msg += f" {datetime.fromtimestamp(batch['completed_at']).strftime("%H:%M:%S")}"
	if batch['in_progress_at']:
		d = batch['in_progress_at'] - batch['created_at']
		msg += f" | W:{timedelta(seconds=d)}"
	msg += "\n"

	# I/O
	msg += f"I: {batch['input_file_id']}\n"
	if batch['output_file_id']:
		msg += f"O: {batch['output_file_id']}\n"
	if batch['error_file_id']:
		msg += f"E: {batch['error_file_id']}\n"

	counts = batch['request_counts']
	if counts:
		msg += f"Cnt: {counts['completed']} E:{counts['failed']} / {counts['total']}"

	return msg

if __name__ ==  "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("-e", "--env", required=True, help="env for HOST, API_KEY")

	subparsers = parser.add_subparsers(dest='api', required=True)

	# Batch: https://developers.openai.com/api/reference/resources/batches
	batch_parser = subparsers.add_parser('b', aliases=['batch'], help="batch")
	batch_commands = batch_parser.add_subparsers(dest='cmd', required=True)
	batch_list = batch_commands.add_parser('ls', aliases=['list'], help="list batches")
	batch_list.add_argument('-i', dest='ing')
	batch_list.add_argument('-f', dest='fail')
	batch_list.add_argument('-c', dest='cancel')
	batch_get = batch_commands.add_parser('cat', aliases=['get', 'retrieve'], help="retrieve batches")
	batch_get.add_argument('id', nargs=1, help="batch id")
	batch_cancel = batch_commands.add_parser('d', aliases=['cancel'], help="cancel batches")
	batch_cancel.add_argument('id', nargs=1, help="batch id")

	# File: https://developers.openai.com/api/reference/resources/vector_stores/subresources/files
	file_parser = subparsers.add_parser('f', aliases=['file'], help="file")
	file_commands = file_parser.add_subparsers(dest='cmd', required=True)
	file_list = file_commands.add_parser('ls', aliases=['list'], help="list files")
	batch_list.add_argument('-a', '--all', action='store_true', help="fetch all")
	batch_list.add_argument('-i', dest='ing')
	batch_list.add_argument('-f', dest='fail')
	batch_list.add_argument('-c', dest='cancel')

	file_get = file_commands.add_parser('cat', aliases=['get', 'retrieve'], help="retrieve file")
	file_get.add_argument('id', nargs=1, help="file id")
	file_delete = file_commands.add_parser('d', aliases=['delete'], help="delete file")
	file_delete.add_argument('id', nargs=1, help="file id")

	args = parser.parse_args()

	load_dotenv(os.path.expanduser(args.env))
	client = OpenAI(
		base_url=os.getenv("API_HOST"),
		api_key=os.getenv("API_KEY"),
	)

	if args.api == 'b': # batch
		if args.cmd == 'ls': # list
			res = client.batches.list()
			batches = res.model_dump()["data"]

			has_more = res.has_more
			while res.has_more:
				time.sleep(0.1)
				print(".", end="", flush=True, file=sys.stderr)
				res = client.batches.list(after=res.last_id)
				batches.extend(res.model_dump()["data"])

			if has_more:
				print("", file=sys.stderr)

			filter = []
			if args.ing:
				filter.append('validating, in_progress, finalizing')
			if args.fail:
				filter.append('failed, expired')
			if args.cancel:
				filter.append('cancelling, cancelled')
			#else completed

			if len(filter) > 0:
				batches = [b for b in batches if b['status'] in filter]

			for batch in batches:
				print(format_batch(batch))
		elif args.cmd == 'cat':
			res = client.batches.retrieve(args.id[0])
			print(format_batch(res.model_dump()))
		elif args.cmd == 'd':
			res = client.batches.cancel(args.id[0])
			print(res.model_dump())
	elif args.api == 'f': # file
		if args.cmd == 'ls': # list
			res = client.files.list(order='desc')
			files = res.model_dump()["data"]

			if args.all:
				has_more = res.has_more
				while res.has_more:
					time.sleep(0.1)
					print(".", end="", flush=True, file=sys.stderr)
					res = client.files.list(after=res.last_id)
					files.extend(res.model_dump()["data"])

				if has_more:
					print("", file=sys.stderr)

			filter = []
			if args.ing:
				filter.append('validating, in_progress, finalizing')
			if args.fail:
				filter.append('failed, expired')
			if args.cancel:
				filter.append('cancelling, cancelled')
			#else completed

			if len(filter) > 0:
				files = [f for f in files if f['status'] in filter]

			for file in files:
				print(file)
		elif args.cmd == 'cat':
			res = client.files.retrieve(args.id[0])
			print(res.model_dump())
		elif args.cmd == 'd':
			res = client.files.delete(args.id[0])
			print(res.model_dump())
