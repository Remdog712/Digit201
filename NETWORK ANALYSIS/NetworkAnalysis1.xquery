let $xml := collection('\SimpsonsFinalFilesXml\Simpsons_S1/?select=*.xml')
let $speakers := $xml//fam

for $s in $speakers
let $episode := $xml[.//ep]
for $eps in $episode
let $epTitle := $eps//epTitle
    let $targets := $epTitle
    let $source := $s ! lower-case(.) ! normalize-space()
    return concat("FAMILY", "&#x9;", $source, "&#x9;", "EPISODE", "&#x9;", $epTitle, "&#10;")
    