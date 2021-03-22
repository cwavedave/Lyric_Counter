import operator

lyrics = """Today is gonna be the day
That they're gonna throw it back to you
By now you should've somehow
Realized what you gotta do
I don't believe that anybody
Feels the way I do about you now
Backbeat, the word is on the street
That the fire in your heart is out
I'm sure you've heard it all before
But you never really had a doubt
I don't believe that anybody
Feels the way I do about you now
And all the roads we have to walk are winding
And all the lights that lead us there are blinding
There are many things that I
Would like to say to you but I don't know how
Because maybe
You're gonna be the one that saves me
And after all
You're my wonderwall
Today was gonna be the day
But they'll never throw it back to you
By now you should've somehow
Realized what you're not to do
I don't believe that anybody
Feels the way I do about you now
And all the roads that lead you there were winding
And all the lights that light the way are blinding
There are many things that I
Would like to say to you but I don't know how
I said maybe
You're gonna be the one that saves me
And after all
You're my wonderwall
I said maybe (I said maybe)
You're gonna be the one that saves me
And after all
You're my wonderwall
I said maybe (I said maybe)
You're gonna be the one that saves me (saves me)
You're gonna be the one that saves me (that saves me)
You're gonna be the one that saves me (that saves me)"""

song = lyrics.split()

def lyrics_frequency(song_lyrics):
    word_frequency = {}
    for word in song_lyrics:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency

song_lyrics = lyrics_frequency(song)

sorted_tuples = sorted(song_lyrics.items(), key=operator.itemgetter(1), reverse=True)
sorted_dict = {k: v for k, v in sorted_tuples}

print(sorted_dict)