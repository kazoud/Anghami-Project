Hello, this is my Anghami project.

For this project, I did two different tasks. 

For the first task, the file main.py contains a friend recommender. The input is the ID and the code looks at the best match of your best match and recommends it to you.

For the second task, it is apparently known in the music industry that most of the modern sounds/hit musics are created using the same 4 chords.

I wanted to see if I could verify this claim using the trending songs on Anghami.

Frequencies.py is the code I used to get the trending songs, and test.py is for the signal processing. The processing was a bit computationally expensive, so I only took international trends.

For each song, I went on youtube and downloaded an mp3 version of the song. I wanted to isolate only the music but most of the songs are so new that a karaoke version does not exist yet. There are softwares like audacity that can separate music from lyrics and I considered using it, but this might result in bad quality music, so I avoided this.

I had to convert from mp3 format to wav files because python can naturally deal with them. I also had to downsample these files by several orders of magnitude because the number of samples was just too large. Because of this, I am extremely unsure about the validity/interpretability of my results. In hindsight, I should have only taken the looping part of the music and process this. Each songs consisted of about 10-13 million samples. I had to downsample to 100 000 samples, so I don't even know if what I processed sounds like the initial songs. 

After the downsampling, I computed the Fast Fourier Transform of my files, and plotted them. They look extremely similar, but I don't think this shows anything significant. The downsampling was sloppy, and I am not even sure how to interpret my plots. In any case, it was a nice experiment to work on.

Thank you for your time, I hope you will like the project.

Best regards,

Karim Dahrouge