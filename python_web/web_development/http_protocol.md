#### HTTP Request GET
```
GET /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3
```
`/path` full url path, `/` means index
`HTTP/1.1` version 1.1
`Host: www.xxx.com`
`\r\n` newline character

#### HTTP Request POST
```
POST /path HTTP/1.1
Header1: Value1
Header2: Value2
Header3: Value3

Body...
```
`\r\n` newline character
`\r\n\r\n` header ends, body starts

#### HTTP Response
```
200 OK
Header1: Value1
Header2: Value2
Header3: Value3

Body...
```
`\r\n` newline character
`\r\n\r\n` header ends, body starts
`200 OK` successful respond
`404 Not Found`
`500 Internal Server Error`
`3xx` redirect
`4xx` client error
`5xx` server error
`Content-Type: text/html`
`Content-Encoding: gzip`
If the browser needs to request for other resources on this page after 
loading the HTML, such as picture, video, Flash, JavaScript, CSS, it 
will send another HTTP request for those contents. This is called the
*request-response model*.
