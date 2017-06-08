"""
cat rt-polaritydata/rt-polarity.pos | awk '{print "+1 "$0}' > rt-polarity.pos
cat rt-polaritydata/rt-polarity.neg | awk '{print "-1 "$0}' > rt-polarity.neg

cat rt-polarity.pos rt-polarity.neg | perl -MList::Util=shuffle -e 'print shuffle(<STDIN>);' > sentiment.txt

cat sentiment.txt | grep -a -e '^+1'| wc -l
cat sentiment.txt | grep -a -e '^-1'| wc -l
"""
