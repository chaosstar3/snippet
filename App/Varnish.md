minimal
```vcl
vcl 4.0;

backend dummy {
	.host = "127.0.0.1";
	.port = "80";
}

sub vcl_recv {
	return (synth(200, "OK"));
}

sub vcl_synth {
	set resp.body = "<html><body>" + resp.status + " " + resp.reson + "</body></html>"
	return (deliver);
}
```

```
sub vcl_recv {
	# if (req.url ~ "^/") {
		set req.backend_hint = be.backend();
	} else {
		return (synth(200, "OK"));
	}
}
```

```
sub vcl_deliver {
	if (obj.htis > 0) {
		set resp.http.X-Cache = "HIT";
	} else {
		set resp.http.X-Cache = "MISS";
	}
}
```