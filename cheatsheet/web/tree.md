```css
:root {
	--connection-line: 2px solid #000000;
	--connection-line-length: 10px;
}

.block {
	width: max-content;
	padding: 1px;
	border: 1px solid black;
	position: relative;
}

.block > div {
	display: inline-block;
	vertical-align: middle;
}
/* horizontal line */
.block:before {
	top: 50%;
	position: absolute;
	width: var(--connection-line-length);
	content: '';
	border-top: 1px solid black;
}

.content {
	margin-right: var(--connection-line-length);
}

.content:after {
	top: 50%;
	position: absolute;
	width: var(--connection-line-length);
	content: '';
	border-top: 1px solid black;
}

```

```css
/* variable default */
:root {
    --connection-line: 2px solid #000000;
    --connection-line-length: 10px;
    --block-margin: 2px;
}
.block {
    width: fit-content;
    text-align: initial;
    /*border: 3px dotted green; /*for debug*/
}

.vtree .children {
    font-size: 0; /* inline-block zero-margin */
    text-align: center;
}
.vtree .block{
    padding: 0 var(--block-margin) 0 var(--block-margin);
    display: inline-block;
    vertical-align: top;
    font-size: initial;
}
.htree .block {
    padding: var(--block-margin) 0 var(--block-margin) 0;
    font-size: 0; /* inline-block zero-margin */
    white-space: nowrap;
}
.htree .block > div {
    display: inline-block;
    vertical-align: middle;
    font-size: initial;
}
/* line from parent */
.children {
    position: relative;
}
.vtree .children {
    margin-top: var(--connection-line-length);
}
.htree .children {
    margin-left: var(--connection-line-length);
}
.children:not(:empty):before {
    content: "";
    position: absolute;
}
.vtree .children:not(:empty):before {
    height: var(--connection-line-length);
    top: calc(-1*var(--connection-line-length));
    left: 50%;
    border-left: var(--connection-line);
}
.htree .children:not(:empty):before {
    width: var(--connection-line-length);
    left: calc(-1*var(--connection-line-length));
    top: 50%;
    border-top: var(--connection-line);
}
/* lines to children */
.children .block {
    position: relative;
}
.children .block:before,.block:after {
    content: "";
    position: absolute;
}
.vtree .children .block {
    margin-top: var(--connection-line-length);
}
.htree .children .block {
    margin-left: var(--connection-line-length);
}
/* spreading line: use :before */
.vtree .children .block:before {
    width: 100%;
    left: 0;
    top: calc(-1*var(--connection-line-length));
    border-top: var(--connection-line);
}
.vtree .children .block:only-child:before {
    width: 0px;
}
.vtree .children .block:first-child:not(:only-child):before {
    left: 50%;
    width: 50%;
}
.vtree .children .block:last-child:not(:only-child):before {
    right: 50%;
    width: 50%;
}
.htree .children .block:before {
    height: 100%;
    top: 0;
    left: calc(-1*var(--connection-line-length));
    border-left: var(--connection-line);
}
.htree .children .block:only-child:before {
    height: 0;
}
.htree .children .block:first-child:not(:only-child):before {
    height: 50%;
    top: 50%;
}
.htree .children .block:last-child:not(:only-child):before {
    height: 50%;
    bottom: 50%;
}
/* line for each child: use :after */
.vtree .children .block:after {
    width: 100%;
    height: var(--connection-line-length);
    left: 50%;
    top: calc(-1*var(--connection-line-length));
    border-left: var(--connection-line);
}
.htree .children .block:after {
    height: 100%;
    width: var(--connection-line-length);
    left: calc(-1 * var(--connection-line-length));
    top: 50%;
    border-top: var(--connection-line);
}
```