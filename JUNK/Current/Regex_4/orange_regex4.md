# Simpsons Regex 4

Alright so some crazy stuff happened. I went off script here

I made another scraper for a different simpsons websites. that all worked and text files are in much better format with actual speakers and curtain cues. My mistake was that I completely forgot to `&` for `&amp;` as well as the `<` `>`

What I did do though was

- `^([A-Z]+):` into `<speaker>\0</speaker>`

- `\b(FADE OUT|CREDITS BEGIN|THE END|FADE IN|CUT TO|DISSOLVE TO|FADE TO BLACK|)\b` into `<stage>\0</stage>`

- and lastly `^(\d{2}x\d{2})(.+)$` into `<episode><episodenumber>\1</episodenumber>\2</epsiode`
 
 The strangest thing about that last Find and Replace is that `^(\d{2}x\d{2})(.+)$` works perfectly on each file by itself but not across all files. I mean it's doable manually but that cuts down on simplicity.

 - Also did not do XML tags as I couldn't figure out how to do it non manually

 *Thanks for reading - from yours truly*
