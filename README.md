# Frequency Filer
## Normal Mode
This program looks for a file called sample.txt. This file will contain the text of a book, part of a book, or speech in plain text format. It reads this file and then returns the top 20 words used in the text and the number of times they are used.

## Hard Mode
Added Features:
 * The following list of common words was removed from results
    * a,able,about,across,after,all,almost,also,am,among,an,and,any,are,as,at,be,
because,been,but,by,can,cannot,could,dear,did,do,does,either,else,ever,every,
for,from,get,got,had,has,have,he,her,hers,him,his,how,however,i,if,in,into,is,
it,its,just,least,let,like,likely,may,me,might,most,must,my,neither,no,nor,
not,of,off,often,on,only,or,other,our,own,rather,said,say,says,she,should,
since,so,some,than,that,the,their,them,then,there,these,they,this,tis,to,too,
twas,us,wants,was,we,were,what,when,where,which,while,who,whom,why,will,with,
would,yet,you,your

 * User is able to specify file to assess on the command line by running `python3 word_frequency.py FILENAME`
