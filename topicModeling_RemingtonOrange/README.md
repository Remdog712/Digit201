# Python Topic Modeling 
## Remington Orange
### 02//08/2023


Okay so what changed? 

- I completely switched my text files from the grimm ones to the recipes from [text](http://www.textfiles.com/food/)

*I used the offered zip file instead of using a scraper so that I could easily delete the non-text files for simplicity.*

### That's where my troubles began

I had to first deal with using `ntlk.download(punkt)` so I could start work on fixing the issue of elements not first included in `UTF`. 

I had to utilize [ChatGPT](https://chat.openai.com/chat) for this part and a few others. 

#### Here's what I used [ChatGPT](https://chat.openai.com/chat) for:
- debugging the cleaning doc process
- figuring out why I had topics issues

*Turns out I had it set to the same "208" when I needed to set it to the "93" files that I had but then THAT didn't work so the best I could get it to run on was "90" so here we are*

Everything else was kinda straight forward

*as straight forward as python gets*

I added other stop words like "c" for cups and such just because they annoyed me as being the number 1 one. Couple other weird ones got slashed just because I get to play as `Pyhton_God`

Everything else was already laid out, just switched where the files were being taken from and making sure everything checked out and so far, I'm happy with the results.

`:)`
