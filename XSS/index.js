const express = require('express')
const path = require('path')
const cookieParser = require('cookie-parser');
const { REPL_MODE_STRICT } = require('repl');

const badwords = ["onactivate",
  "onafterprint",
  "onafterscriptexecute",
  "onanimationcancel",
  "onanimationend",
  "onanimationiteration",
  "onauxclick",
  "onbeforeactivate",
  "onbeforecopy",
  "onbeforecut",
  "onbeforedeactivate",
  "onbeforepaste",
  "onbeforeprint",
  "onbeforescriptexecute",
  "onbeforeunload",
  "onbegin",
  "onblur",
  "onbounce",
  "oncanplay",
  "oncanplaythrough",
  "onchange",
  "onclick",
  "onclose",
  "oncontextmenu",
  "oncopy",
  "oncuechange",
  "oncut",
  "ondblclick",
  "ondeactivate",
  "ondrag",
  "ondragend",
  "ondragenter",
  "ondragleave",
  "ondragover",
  "ondragstart",
  "ondrop",
  "ondurationchange",
  "onend",
  "onended",
  "onerror",
  "onfinish",
  "onfocus",
  "onfocusin",
  "onfocusout",
  "onfullscreenchange",
  "onhashchange",
  "oninput",
  "oninvalid",
  "onkeydown",
  "onkeypress",
  "onkeyup",
  "onload",
  "onloadeddata",
  "onloadedmetadata",
  "onloadend",
  "onloadstart",
  "onmessage",
  "onmousedown",
  "onmouseenter",
  "onmouseleave",
  "onmousemove",
  "onmouseout",
  "onmouseover",
  "onmouseup",
  "onmousewheel",
  "onmozfullscreenchange",
  "onpagehide",
  "onpageshow",
  "onpaste",
  "onpause",
  "onplay",
  "onplaying",
  "onpointerdown",
  "onpointerenter",
  "onpointerleave",
  "onpointermove",
  "onpointerout",
  "onpointerover",
  "onpointerrawupdate",
  "onpointerup",
  "onpopstate",
  "onprogress",
  "onreadystatechange",
  "onrepeat",
  "onreset",
  "onresize",
  "onscroll",
  "onsearch",
  "onseeked",
  "onseeking",
  "onselect",
  "onselectionchange",
  "onselectstart",
  "onshow",
  "onstart",
  "onsubmit",
  "ontimeupdate",
  "ontoggle",
  "ontouchend",
  "ontouchmove",
  "ontouchstart",
  "ontransitioncancel",
  "ontransitionend",
  "ontransitionrun",
  "ontransitionstart",
  "onunhandledrejection",
  "onunload",
  "onvolumechange",
  "onwaiting",
  "onwebkitanimationend",
  "onwebkitanimationiteration",
  "onwebkitanimationstart",
  "onwebkittransitionend",
  "onwheel",
  "abbr",
  "acronym",
  "address",
  "animate",
  "animatemotion",
  "animatetransform",
  "applet",
  "area",
  "article",
  "aside",
  "audio",
  "base",
  "basefont",
  "bdi",
  "bdo",
  "bgsound",
  "big",
  "blink",
  "blockquote",
  "body",
  "button",
  "caption",
  "center",
  "cite",
  "code",
  "col",
  "colgroup",
  "command",
  "content",
  "custom tags",
  "data",
  "datalist",
  "del",
  "details",
  "dfn",
  "dialog",
  "dir",
  "discard",
  "div",
  "element",
  "embed",
  "fieldset",
  "figcaption",
  "figure",
  "font",
  "footer",
  "form",
  "frame",
  "frameset",
  "head",
  "header",
  "hgroup",
  "html",
  "iframe",
  "image",
  "img",
  "input",
  "ins",
  "isindex",
  "kbd",
  "keygen",
  "label",
  "legend",
  "link",
  "listing",
  "main",
  "map",
  "mark",
  "marquee",
  "menu",
  "menuitem",
  "meta",
  "meter",
  "multicol",
  "nav",
  "nextid",
  "nobr",
  "noembed",
  "noframes",
  "noscript",
  "object",
  "optgroup",
  "option",
  "output",
  "param",
  "picture",
  "plaintext",
  "progress",
  "rtc",
  "ruby",
  "samp",
  "script",
  "section",
  "select",
  "set",
  "shadow",
  "slot",
  "small",
  "source",
  "spacer",
  "span",
  "strike",
  "strong",
  "sub",
  "summary",
  "sup",
  "svg",
  "table",
  "tbody",
  "template",
  "textarea",
  "tfoot",
  "thead",
  "time",
  "title",
  "track",
  "var",
  "video",
  "wbr",
  "xmp"]

const app = express()
app.use(express.urlencoded())
app.use(cookieParser());

var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database(path.join(__dirname + "/sqlite/mdr.db"));

db.run("CREATE TABLE IF NOT EXISTS reports (`id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, `description` CHAR(256) NOT NULL, `read` BOOLEAN default 0)")

app.get('/', function (req, res) {
    res.sendFile(path.join(__dirname + "/html/form.html"))
})
  
app.post('/tickets', function (req, res) {
    request = "INSERT INTO reports (description) VALUES (?);"
    my_value = req.body.description
    values = [my_value]
    bad = false;
    console.log(my_value)
    
    for (const word in badwords)
      if (my_value.toLowerCase().includes(badwords[word]))
        bad = true;
    
    res.status(406);
    if (!bad) {
      res.status(202); 
      db.run(request, values, function(err) {
        if (err) {
          res.status(500).send();
          return;
        }
        console.log(`A row has been inserted with rowid ${this.lastID}`);
      })
    }
    res.sendFile(path.join(__dirname + "/html/form.html"))
})

app.get('/admin', function (req, res) {
   db.all("SELECT * FROM reports WHERE read=0 LIMIT 1", [], (err, rows) => {
        if (err) {
          throw err;
        }
        if (rows.length == 0 || req.cookies == null || req.cookies.session != "eyJpZCI6MX0.XeD94w.3oC__mzIIRdsxn1WXyMdJh7HQlg") {
          res.send("You are not supposed to be here.");
          return;
        }
        db.run("UPDATE reports SET read=1 WHERE id=? ", [rows[0].id], (error) => {
          if (error) {
            throw error;
          }})
        res.send(rows[0].description)
      })
})

app.listen(3000, function () {
    console.log('Example app listening on port 3000!')
})
  