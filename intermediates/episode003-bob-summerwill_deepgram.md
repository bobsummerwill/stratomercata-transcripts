**SPEAKER_00:**
[0.0s] Alrighty.
[1.1s] Well, thanks everyone for coming back .
[1.1s] We've done a couple of videos.
[5.5s] So we've done two on the early days of Ethereum,
[9.8s] and I actually did another video on identity following that, which you can check out on my channel.
[15.7s] And,
[16.9s] in the process, we're excited to reconnect with Bob Summerwell .
[16.9s] So,
[22.5s] Bob will ask to introduce himself in a second, but, he actually went quite in-depth,
[28.8s] you know, in in in reaction to the videos and helping to work together to patch up the whole story from our collective memory on the early days of Ethereum, wrote a long blog post that, you should check out, and we'll link in the notes .
[28.8s] And
[42.6s] we asked him to join us here today to kinda dig more into the story and also just generally catch up .
[42.6s] So with that,
[50.2s] maybe
[51.2s] I'll
[52.4s] hand it to Bob to do a quick intro, and we can just kinda get into it.

**SPEAKER_01:**
[57.0s] So, yeah, hi .
[57.0s] You know, thanks so much for the invite .
[57.0s] You know, like I said to you guys,
[62.6s] you know, I love those first two videos .
[62.6s] You know, I'll I I I love this history,
[68.5s] and it was great to,
[70.8s] you know, both hear that and and have, you know, a slightly different perspective as well .
[70.8s] You know, our paths have overlapped in some ways and haven't in others.
[78.5s] So, you know, there are a few things that came up, which I, you know, I I I wasn't myself aware of.
[84.9s] I mean, just for just for everyone's background
[88.9s] about about me and who I am.
[92.0s] So I
[94.9s] got interested
[96.6s] in blockchain in 2014,
[98.3s] but it was 2015 where I really, like, kinda jumped in.
[102.0s] And that happened because I was I was working in Toronto .
[102.0s] I had a six month contract.
[106.8s] I was working in Toronto
[108.8s] around the same time that Ethereum
[111.5s] was doing a mainnet launch.
[114.3s] And I'd actually met Vitalik for the first time in 2014,
[117.5s] but, you know, just kind of following along a little bit, not actually doing anything.
[121.4s] But then moving to Toronto, it's just like orders of magnitude, more stuff going on and,
[126.9s] you know, meetups and, you
[129.6s] know,
[130.8s] Bitcoin
[131.8s] decentral,
[132.7s] coworking space and everything.
[134.6s] So I got, like, really very addicted
[137.4s] through that year, and it was like, right .
[137.4s] I can't not get involved .
[137.4s] Right ?
[137.4s] It's like it's like you're there at the birth of the web or whatever, and you've, you know, you've you've met Tim Berners Lee, and he's about to, like, go live on the web .
[137.4s] And it's like, you know, how can you not, like, wanna get involved?
[152.8s] So I just started
[154.6s] sort of volunteering
[157.4s] and helping.
[158.7s] My background prior to that was in the games industry, so, like, fifteen years of c plus
[164.7s] fifteen years of c plus plus .
[164.7s] So
[167.7s] I was like, well, you know, I can I can do something with with CPP Ethereum?
[172.8s] And I was really into mobile and wearables .
[172.8s] So my first thing I set myself is, you know, can I get Ethereum running on my smartwatch?
[180.5s] You know, could you get a smartwatch and go around it like, ping, there's some money ?
[180.5s] You know, that'd be really cool.
[185.9s] So
[187.5s] so, yeah, I just started doing stuff on there .
[187.5s] That was about the time that that Gav was
[193.6s] parting company
[195.1s] with with the foundation as well .
[195.1s] So there was kind of a dearth of people on that team.
[203.5s] So,
[204.3s] you know, like that period, I ended up being, like, I think the only person in the world who was actually helping on that.
[211.5s] Like, you know, no companies,
[213.5s] no no nobody was helping.
[216.4s] And then I ended up getting hired into the foundation in early twenty sixteen.
[222.8s] And,
[223.7s] yeah, I've been involved
[225.8s] on
[226.7s] Ethereum Enterprise, Ethereum Hyperledger,
[229.4s] then more recently,
[231.9s] Ethereum Classic.
[233.7s] It's nearly a decade now.

**SPEAKER_02:**
[236.7s] Yeah .
[236.7s] Bob, I I well, and to be open to everyone, like, we're old friends,
[243.8s] and we're happy to have you as our first guest who's on this thing .
[243.8s] But, also,
[249.8s] you are like, you know, the Nelson Mandela of the Ethereum Ecosystem .
[249.8s] You you're friends with everyone .
[249.8s] You know ?
[249.8s] You got you've been in everywhere.
[258.9s] You know ?
[258.9s] Like, so it's great to have your perspective on things.

**SPEAKER_01:**
[262.8s] Thank you.

**SPEAKER_02:**
[264.8s] So I and for as Karen has mentioned, for anyone who hasn't seen Bob's blog post, it's
[272.9s] notionally a blog post, almost a full novel, probably a novella size .
[272.9s] It has pictures of a lot of the people we're talking about.
[280.7s] You dug up so much content out of there .
[280.7s] Were those your personal pictures ?
[280.7s] It's just stuff .
[280.7s] Yeah .
[280.7s] Yeah .
[280.7s] Just stuff I I I I had.

**SPEAKER_01:**
[289.8s] I mean, another
[291.3s] thing here is
[293.5s] there there's a couple of
[297.2s] articles on my own blog from earlier that I linked into there as well,
[302.2s] which was there's one called Ethereum Foundation People and one called Ethereum Foundation Timeline.
[307.6s] So I made those in late twenty seventeen, early twenty eighteen
[313.9s] because there was no canonical history of any of this .
[313.9s] Yeah .
[313.9s] It's like, how did Ethereum start ?
[313.9s] I mean, it's in people's heads .
[313.9s] It's all secondhand stories that you hear from people that were around, but, you know, it's like,
[326.2s] what's true, what isn't.
[327.9s] Because I think, especially on that, like, foundation side,
[332.1s] it was such a mess .
[332.1s] Right ?
[332.1s] Just like
[335.5s] all different people weren't getting on, blowing up,
[339.9s] kind of like
[341.8s] parity versus the foundation
[344.0s] and and Charles, you know, and they're like, god .
[344.0s] What you know ?
[344.0s] So
[348.3s] it I think some people had almost taken this position
[352.0s] of, like, we don't talk about that .
[352.0s] Right ?
[352.0s] Right .
[352.0s] Just because anything I say, like, it's gonna offend somebody else .
[352.0s] So just la la la .
[352.0s] It doesn't matter that you know?
[363.2s] But
[364.3s] but yeah .
[364.3s] So I started gathering that list of, well, you know, who were the people that were around in the pre foundation days and then in in that .
[364.3s] And
[374.0s] so, yeah, I've got this got this one page, this people page, which I think is really cool .
[374.0s] Just it's got so that's basically from 2013
[382.7s] through to early twenty eighteen
[385.5s] identifying
[386.8s] anyone that I could that was involved with Ethereum
[391.1s] Free Foundation
[392.3s] or who worked for the foundation in those early years.
[396.1s] And one of the things that's really great there is Devcon Zero,
[401.1s] which happened in, I think, October
[404.2s] 2014.
[405.7s] So that was the very first Devcon, but it was a closed event .
[405.7s] That wasn't a public event.
[410.4s] Yeah .
[410.4s] And it was
[412.5s] it was foundation people at that time, but there were also, you know, some other key community sorts of people there as well.
[421.2s] And they did this one thing at the start that was introductions.
[425.4s] So there's this video that's about fifteen or twenty minutes long of everybody,
[430.5s] like, hi .
[430.5s] I'm glad I'm here doing, you know, proof of stake research.
[436.2s] Just see these these, you know, so young, so many people that, you know, like, early twenties
[441.7s] Yeah .
[441.7s] You know, and turning up, and it's like, that's, you know,
[446.0s] that that's so and so .
[446.0s] Right ?
[446.0s] And and some of these people as well, you know, they they they're not involved anymore .
[446.0s] You know, they're they're they're sort of like footnotes in history, but but but you have that record.
[456.1s] And
[457.9s] so, yeah, that that that list of people I got I I I got all of that together, and the the the reason that that came about was
[466.9s] in late twenty seventeen, I got a message from Laura Shin
[471.6s] saying, hey .
[471.6s] I hear Ming's being sacked at the foundation .
[471.6s] Like, do you know anything about this ?
[471.6s] Right .
[471.6s] And I said, well, no .
[471.6s] I don't,
[479.9s] but it wouldn't surprise me.
[482.5s] But,
[484.6s] you know, basically, it'd be like Vitalik or maybe Hudson could tell you, but nobody nobody else could tell you .
[484.6s] Anyway and, know, it sort of came out .
[484.6s] Well, yeah, she's, you know, she's not been sacked, but she's agreed to leave .
[484.6s] Right .
[484.6s] And then it's like, well, what's what's next?
[499.9s] So I contacted Vitalik and said, you know, hey .
[499.9s] Is there anything I can do to help ?
[499.9s] You know ?
[499.9s] What can I do?
[505.7s] You know ?
[505.7s] And he said, well, the one thing you can do is can you, like, try and talk to people
[511.0s] and work out, like, you know, what would good look like ?
[511.0s] Right .
[511.0s] What do people think a good Ethereum Foundation would look like?
[518.3s] And so that started my sort of adventure really of, right .
[518.3s] I'm gonna go and talk to all the founders, all the other people, and try and work out, like, you know, what what
[527.5s] and then that just turned into really a mind you know, a thought experiment on my side of, like, okay.
[534.0s] So, you know, to my mind, Bing was terrible.
[538.0s] So how did she get hired?
[540.4s] Like, what was going on,
[542.8s] you know, whatever, two and a half years back that that looked like a good option?
[547.6s] You know ?
[547.6s] Like, what how how did it work before ?
[547.6s] You know ?
[547.6s] Like, what how did the foundation come about ?
[547.6s] And, like, what what were the group of leaders and, like, what were all the dynamics between all of these people ?
[547.6s] So,
[559.6s] yeah, I went down quite a rabbit hole there, and that's that was the the the sort of the genesis for that information gathering.
[567.4s] And I learned a lot.
[571.2s] And
[572.7s] that information as well I gave to Laura and to the other two authors that were doing their Ethereum books is kind of like, right .
[572.7s] There is no canonical,
[581.0s] but this is kind of what I found, which is maybe, like, the best information that there was at that time .
[581.0s] Yeah.

**SPEAKER_02:**
[588.8s] Well and and, also, it's to your point .
[588.8s] It's that I think generally people have sort of survivorship bias about,
[596.2s] you know, like, everything works smooth, but innovation
[599.2s] is messy .
[599.2s] You know, it's messy and it's like, you know, there are million and one different paths that things could have went to, and we just want to kind of acknowledge all that .
[599.2s] Like, you know, like, given where the ecosystem is today,
[613.2s] And even though, you know, it's amazing to me that so many people know about it, that, you know, I spent we all spent the first years trying to get anyone to listen to us talk about blockchain and no one, you know, everyone just glaze over .
[613.2s] Right ?
[613.2s] So it's just kind of nice to take that retrospective view at this point.
[630.8s] Oh,

**SPEAKER_01:**
[631.7s] went a little bit farther along .
[631.7s] It took Blurred out .
[631.7s] We'll just go with it .
[631.7s] Yeah .
[631.7s] One of the things that I I know that the talent said, again, it was maybe in Laura Shin's book, was
[643.8s] like the the founding
[646.3s] of Ethereum
[648.2s] was very atypical
[651.6s] because it was essentially like,
[654.3s] here's here's a white paper out to a bunch of random people
[659.5s] who may be interested,
[661.6s] and it's, like, basically, like, first people that turn up right, your founders.
[666.5s] Like, you know, a a number of them, they'd,
[669.9s] you know, they've not even met each other before .
[669.9s] They've, you know, not really a lot of knowledge.
[676.0s] And
[677.2s] so, yeah, like, there were lots of
[680.8s] interpersonal
[681.7s] things that just didn't work at all .
[681.7s] It's just like,
[685.1s] no,
[686.0s] like, founding a company,
[688.1s] and I'm sure you guys have, you know, have this experience yourself .
[688.1s] Right ?
[688.1s] You wanna start with people that you kind of know and trust a bit because you know that you're going through the fire together .
[688.1s] So, you know, you better have some
[701.5s] stickability with you and,
[705.4s] you know, common alignment
[707.3s] or at least
[709.9s] knowing that you've got good communication to go through those bad times .
[709.9s] Right ?
[709.9s] You you know, that you know that you can work it out .
[709.9s] Yeah .
[709.9s] And what seemed to happen on Ethereum was absolutely the polar opposite of that .
[709.9s] It's just random bunch of people who were there, didn't really know each other, like,
[725.9s] make that commitment before you even know what you're even doing .
[725.9s] Right ?
[725.9s] Yeah .
[725.9s] And so

**SPEAKER_00:**
[731.8s] that didn't work so great .
[731.8s] And I think also Let me actually I I wanted to ask about that .
[731.8s] I'm also just looking at the list of the Ethereum Foundation people, which is remarkably
[742.1s] long for the type of initiative it was.
[745.9s] You know, we we talk about this because we're a management team, and we're trying to get people to focus on particular goals and things our company wants to do and such .
[745.9s] Do you think there is any benefits to this level of you could call it disorganization
[759.5s] or just you know?
[761.2s] I
[762.7s] kind of think
[764.2s] if there were,
[766.0s] know, a benefit and it wasn't merely just an inefficient and painful process that Ethereum succeeded in spite of, It's kind of it embodied the ethos, and it it let people like, put the idea out there, and then people fought for its destiny .
[766.0s] Like, Ethereum existed,

**SPEAKER_03:**
[782.8s] and then they wanted to be part of taking it to and he saw this with the clients and all that too .
[782.8s] Sorry, Jim .
[782.8s] Go ahead .
[782.8s] I was gonna say it kinda worked like a blockchain works, in fact .
[782.8s] Yeah .
[782.8s] Lots of random people coming together with some underlying principle to organize things, and then they fight it out .
[782.8s] But what's that law that organization

**SPEAKER_02:**
[800.4s] technology
[801.5s] reflects the organization?
[803.4s] Law,
[804.4s] I think .
[804.4s] So, yeah, something like that .
[804.4s] Like yes .
[804.4s] Sorry .
[804.4s] Mhmm.

**SPEAKER_01:**
[809.6s] Yeah .
[809.6s] I mean, I I
[812.2s] I guess, in general, yes .
[812.2s] You know, having that, like, frothing emergent,
[817.4s] like, stuff is is good.
[819.9s] I think where it was really screwed, though, was to do with money and and, you know, the ICO funding .
[819.9s] Right ?
[819.9s] That it's basically like, okay .
[819.9s] Here, we're doing the thing .
[819.9s] And here, the money is all actually in this organizational group.
[834.1s] And the people in that group are being funded, you know, are in this privileged position.
[840.2s] It it's something which
[843.0s] Brian said to me in later years was it's sort of like the original sin of Ethereum
[849.0s] is
[849.9s] if you wanna have that kind of collaboration.
[852.7s] So, you know, whatever stuff like the EA and Hyperledger or even just, you know, the rather looser protocol development around Ethereum,
[861.2s] you don't wanna pay
[863.4s] one team
[865.3s] and not the others.
[866.9s] Right .
[866.9s] Because that just
[868.6s] screws that battlefield.
[870.7s] So
[872.4s] you have this situation, for example, where,
[877.2s] you know, you got the c plus plus client, you've got a Geth.
[880.5s] You you know, you did have the Python client as well, so you have that good triangulation, but it was essentially like the the the funded ones were were c plus plus and Go.
[889.5s] And then they have the the money crisis of of of, like, oh my god .
[889.5s] Is this thing even gonna happen ?
[889.5s] Right .
[889.5s] We've got cutscope .
[889.5s] C plus plus is gone.
[897.9s] Gab ends up going out of the way .
[897.9s] And then you have parity,
[902.6s] you know, having one of the major clients
[905.2s] but without funding.
[907.1s] So it's like, Geth .
[907.1s] Oh, Geth .
[907.1s] That's the, you know, that's the favored child .
[907.1s] Right ?
[907.1s] You know, that's the it's not like
[914.6s] the official client, but it is the official client.
[918.5s] So all that sort of, like,
[921.6s] separation of implementation versus specification
[925.1s] and, you know, in that free market around that
[928.4s] was really skewed
[930.1s] because the money was with Geth, and Geth were in the foundation,
[933.7s] and they've got, you know, Vitalik's kind of blessing and everything.
[937.6s] So I I think that's where things were great
[942.5s] because you did have the diversity, but it wasn't fair diversity.
[946.9s] And I think if you look at what's happening now on
[950.6s] the consensus
[952.2s] clients
[953.5s] for,
[954.5s] I was gonna say, ethereum two .
[954.5s] It's not called ethereum two anymore .
[954.5s] But, you know, the separation that you have with those execution clients and consensus clients,
[962.8s] none of those consensus clients are made by the foundation.
[966.6s] The foundation doesn't have client teams.
[969.6s] They they do funding .
[969.6s] Like, they got the grants, and I think all of those teams are gonna be grant recipients.
[975.0s] So that's kind of centralization in a way,
[978.4s] but it is an even playing field in terms of the development .
[978.4s] Right ?
[978.4s] Because you've got unevenness of funding, and that wasn't the case,
[986.6s] you know, originally for Ethereum.
[989.5s] And I think that that made a lot of bitterness as well because it's like, well, why do you guys got the money ?
[989.5s] Like, we're we're making another one as well and
[997.1s] or or, you know, other parts
[1000.1s] of the ecosystem .
[1000.1s] Like, there wasn't a grants program for a number of years .
[1000.1s] Yeah .
[1000.1s] Between about 2015 and 2018, there wasn't even a grants program.
[1008.1s] You know, you've got the foundation sitting on hundreds of millions of dollars, and teams couldn't even get funded for doing anything.
[1014.6s] So
[1016.9s] so, yeah, I think the diversity is good, but the money was bad.

**SPEAKER_00:**
[1023.1s] Interesting .
[1023.1s] Yeah .
[1023.1s] I I think
[1025.9s] alright .
[1025.9s] Okay .
[1025.9s] That's a it's a good strong point .
[1025.9s] So if you compare it to, like, a Bitcoin,
[1030.3s] which I know less about the history of the development of Bitcoin, but it was kind of similar.
[1035.7s] There was less of a
[1038.0s] there was no
[1039.6s] pre mine and no
[1041.7s] token presale.
[1043.7s] And so
[1045.0s] the people who are in it were in it for general interest, and it was
[1050.4s] really sincerely,
[1051.8s] an even playing field .
[1051.8s] And I I would argue, you know, in
[1056.6s] in some ways, Ethereum has made bigger strides than Bitcoin, especially since,
[1061.0s] you know, let's say, 02/2015.
[1063.4s] Some of the value prop of Bitcoin is that it never changes, and it's kind of part of why it holds its value in some way .
[1063.4s] And but it's, I think,
[1073.3s] you know, been stifled a little bit for that reason .
[1073.3s] I I think it's pretty hard probably to
[1080.5s] make step function positive changes
[1083.1s] in a fully decentralized
[1084.7s] manner.

**SPEAKER_01:**
[1086.0s] Another
[1087.1s] major difference there talking about clients is
[1090.5s] it was a very deliberate decision, right, on Ethereum to to separate the specification from the clients.
[1096.9s] Yeah .
[1096.9s] And that there were multiple clients from day one.
[1100.6s] I I've see if I can find my Twitter thread .
[1100.6s] I was finding these the other day .
[1100.6s] I was finding the first commits
[1106.9s] for
[1107.8s] for PyEthereum,
[1109.4s] PyApp,
[1111.1s] or PyEthereum as it was, CPP Ethereum, and and Go Ethereum.
[1115.4s] And they were all
[1119.0s] I think they were all November or December .
[1119.0s] I think they were all 2013,
[1123.1s] not even 2014 for those three .
[1123.1s] Yeah .
[1123.1s] And then Ethereum j looked like it started in about April,
[1129.9s] I think.

**SPEAKER_02:**
[1131.0s] But, you know, that was Yeah .
[1131.0s] Jim, Karen, you guys started Ethereum h in 2014.

**SPEAKER_00:**
[1136.2s] Right ?
[1136.2s] Yeah .
[1136.2s] We were much later .
[1136.2s] We were

**SPEAKER_03:**
[1140.6s] When did we get the fourth quarter twenty fourteen ?
[1140.6s] Yeah .
[1140.6s] That's Sounds appropriate.

**SPEAKER_00:**
[1147.1s] And I had worked on Ethereum just in the summer, so starting kind of
[1151.8s] maybe June
[1153.1s] 2014.
[1154.5s] I got to know the project pretty well .
[1154.5s] And then I'd I'd gone back to Berkeley.
[1159.5s] I was in New York for the summer and met Jim
[1163.5s] September, October, something like that, and we started work more or less right away .
[1163.5s] More Jim than me .
[1163.5s] But
[1170.3s] so, yeah, so there was a big time delay on on our side .
[1170.3s] And and, yeah, I think okay .
[1170.3s] Yep .
[1170.3s] Bob, it it's an interesting point .
[1170.3s] Right ?
[1170.3s] I think probably
[1178.6s] they could have
[1182.3s] there was some some real mismanagement at different times both with the running out of funds,
[1187.0s] doing any hedging.
[1188.5s] And then later,
[1189.9s] I I guess I agree that it could have just been more fair and open feeling, and that would have alienated fewer people, and it could have even just been bigger than it is today .
[1189.9s] Obviously, we're talking about a smashing success here,
[1203.4s] but it it's sort of the
[1206.1s] idea and the community
[1207.9s] was so powerful that it you know, there's definitely succeeded in in spite of aspect .
[1207.9s] I think there was value still in this, like, throw it out there, get people to fight over it, but
[1220.5s] it it probably overcorrected,
[1222.8s] and lots of these people also just went and started their own thing

**SPEAKER_01:**
[1226.5s] because it wasn't the big enough time .
[1226.5s] I mean, the other thing is right at the start there .
[1226.5s] It's like, well, the people that doing it, that was the whole world .
[1226.5s] Right ?
[1226.5s] You know, that was everything, right, was
[1237.3s] several month I mean, all of that early work on the clients actually was before the foundation even existed .
[1237.3s] That was actually unfunded.

**SPEAKER_02:**
[1244.1s] Yeah.

**SPEAKER_01:**
[1246.1s] Because I'm looking at the dates .
[1246.1s] So the the white paper came out in November
[1251.0s] 2013
[1252.2s] sorry, 2013.
[1254.5s] PyEthereum
[1255.4s] was started on 11/19/2013.
[1260.2s] Gav actually was in contact with Vitalik on that same day.
[1264.8s] CPP Ethereum started four days later, twenty third of of December .
[1264.8s] Obviously, some over Christmas hacking on these things
[1273.7s] going on.
[1275.2s] And then Go Ethereum
[1277.7s] was December 26, so just three further days.
[1282.9s] The foundation
[1284.7s] got formed, I think, in May
[1289.3s] or May 2014,
[1291.4s] but the crowdsale didn't conclude until September
[1294.3s] 2014.
[1295.3s] So you'd actually got about nine months worth of development
[1299.0s] on all of these three clients that was actually unfunded.
[1303.5s] So,
[1304.7s] you know, make make you know, I think I think that unfairness kinda came in a little bit later .
[1304.7s] I think for that phase, it was like nobody got funded.
[1312.9s] Oh,
[1313.9s] sorry.
[1314.8s] You
[1315.7s] know, nobody got funded, though there was the retrospective payback .
[1315.7s] Right?
[1320.0s] You know, when when the crowdsale had gone through, you had,
[1323.8s] you know, money for early contributors,
[1327.0s] which I think I think that was nearly 10%
[1329.9s] Yeah .
[1329.9s] For, like, a hundred, hundred and twenty people.
[1333.8s] Like, some people made out, like, absolute bandits for for those early months.
[1339.0s] But
[1340.5s] then, yeah, following that,
[1342.9s] there was hiring of actual, you know, staff
[1347.0s] onto those teams.
[1349.5s] And that, I think, is when it became kind of uneven
[1352.6s] because you already had a for a number of months there and that, you know, that that never got funded .
[1352.6s] And then you
[1359.4s] and then you guys
[1361.0s] starting
[1361.8s] whenever you were starting.
[1364.2s] So, yeah, it it kind of became uneven, I think, at that point .
[1364.2s] And and and the probably the worst of it of all was for parity,
[1372.2s] you know, when when that team spun out and you basically did have a major,
[1377.2s] you know,
[1378.4s] rapidly load bearing client,
[1382.2s] and it was just, you know, unfunded,
[1385.2s] especially in with Geth who was, you know,
[1389.2s] had been the CTO and wrote the yellow paper and had the first working client and, you know, all of the value he delivered .
[1389.2s] And then it's like, right .
[1389.2s] Sorry .
[1389.2s] You're out, and you're not getting any money .
[1389.2s] You know?

**SPEAKER_00:**
[1400.4s] Yes .
[1400.4s] Do you
[1402.6s] so my memory
[1404.1s] around the c plus plus client was that
[1407.2s] there were funds to
[1409.3s] do a security audit
[1411.2s] for
[1413.0s] two clients,
[1414.4s] but one at a time, and it was tight .
[1414.4s] Right ?
[1414.4s] Like And so they did go Ethereum first, and I think they did actually do the security audit on CPP Ethereum,
[1424.3s] but I'm not quite sure .
[1424.3s] I'm not they sure did .
[1424.3s] You know ?
[1424.3s] You know mean ?
[1424.3s] Maybe

**SPEAKER_01:**
[1429.5s] maybe there'd been an intention to do that, but then the money ride ran out before it happened.
[1437.0s] I mean, my understanding in terms of uptake as well is CPP Ethereum was, like, working first,
[1444.2s] but then Go Ethereum just, like, caught up and overtook it, like, really fast.
[1449.6s] So
[1450.8s] when they were making those decisions on cutting funding, which would have been
[1456.1s] mid
[1457.0s] twenty fifteen,
[1458.7s] it's like,
[1460.2s] hey, Gabby, you're the CTO, but it's your co co pays that's gotta copy it.
[1464.9s] And then
[1466.0s] that's what happened .
[1466.0s] And

**SPEAKER_03:**
[1468.4s] I mean, I was I was sort of building
[1471.1s] the various clients quite a bit because I was trying to integrate with them at the time.
[1475.8s] And my memory was that the c plus plus client had all the newest stuff in it first .
[1475.8s] So if I wanted to see something first, I would go there.
[1483.5s] But the Go client was more stable.
[1485.9s] Like, because I think because they were putting so much stuff into the c plus plus client, it was often in an unstable situation.
[1492.5s] And so I would typically kinda go to c plus plus first to see the new stuff, but if it wasn't building that day, I would run over to go and try it out .
[1492.5s] Yeah .
[1492.5s] I mean and and that would make complete sense because the other thing to know

**SPEAKER_01:**
[1505.0s] with the c plus plus client is that would that was where the test suites were done.
[1510.2s] You know, like, all the all the tests were generated out of that code base .
[1510.2s] So as you say, all of the protocol changes
[1517.3s] or whatever would happen there first,
[1520.0s] then you do the test generation through that, and then those are the tests for for
[1525.2s] for other clients.
[1527.2s] So even when CPP Ethereum
[1529.8s] as a client,
[1531.5s] like, died,
[1533.7s] it didn't die within that testing suite for years.
[1537.8s] It's like, right .
[1537.8s] Even though nobody's actually, like, running this or using it on mainnet or anything,
[1542.9s] you know, we've gotta keep we've gotta keep maintaining that one because that's where the the tests are coming from.
[1549.6s] So, yeah, that that that frontline was really, like, leading
[1553.9s] across
[1554.8s] sol c,
[1556.0s] the tests,
[1557.5s] and CPP Ethereum.
[1559.7s] You know, all of those actually were bundled together into a single workspace as well with all of the gooey apps, like with mix and Alice
[1567.6s] zero, Alice one, five.
[1570.3s] Like, it took twenty four hours to build the bloody thing,
[1574.6s] but
[1575.5s] that will be because it was all around Gav .
[1575.5s] Right ?
[1575.5s] You know, Gav was leading all of that .
[1575.5s] You know, he was he was building that client .
[1575.5s] He was writing the yellow paper .
[1575.5s] He was,
[1583.8s] you know, working there with with with Christian and
[1587.4s] and Christophe
[1589.4s] on that specification and testing stuff like that .
[1589.4s] You know, all of that was was there.
[1596.0s] And then on Geth on
[1598.3s] Jeff's side, you know, it's but, you know, just just doing Geth .
[1598.3s] Right ?
[1598.3s] It wasn't wasn't a broader thing.
[1605.1s] And and that that Geth team were working
[1608.1s] closer with Mist, you know, with on Mist.
[1611.7s] Like, for a for a good while, I don't think CPP Ethereum even worked with Mist .
[1611.7s] You know, it's like Yeah .
[1611.7s] All these groups not really talking to each other.
[1621.4s] But but, yeah, that would make sense .
[1621.4s] Like, a lot of it was was Gav led.

**SPEAKER_02:**
[1627.7s] And and
[1629.1s] wait .
[1629.1s] So
[1630.5s] see the Solidity compiler.
[1633.0s] That was part of that c plus plus group too ?
[1633.0s] Yeah .
[1633.0s] That makes sense because it it was written in c plus plus .
[1633.0s] But Yeah .
[1633.0s] It was all under web three umbrella.

**SPEAKER_01:**
[1643.4s] Okay.
[1644.2s] I remember web three umbrella .
[1644.2s] I remember the web three umbrella .
[1644.2s] Yes .
[1644.2s] So, yeah, web three umbrella was a a Git repo with sub repos for,
[1656.3s] you know, for for f .
[1656.3s] It was called f .
[1656.3s] It was just called f, the executable .
[1656.3s] So you'd have f and, again, but,
[1663.6s] yeah, you had f .
[1663.6s] You had sol c.
[1666.7s] You had
[1668.6s] mix, which was the original IDE.

**SPEAKER_03:**
[1671.9s] Yes.

**SPEAKER_01:**
[1675.5s] Acute
[1678.1s] client.
[1679.1s] You had,
[1680.5s] which was the gooey miner.
[1683.0s] Yeah .
[1683.0s] That's right .
[1683.0s] So it's like, here, here's a good press the mine button and you know?
[1689.1s] And then you had one,
[1691.0s] which was sort of
[1693.6s] I guess it was, like, kind of like a gooey client runner thing .
[1693.6s] I can't remember the exact scope,
[1700.0s] but but it was sort of like, right .
[1700.0s] You're running a node,
[1703.1s] but you've kind of got a gooey on it .
[1703.1s] And I I can't remember what it had, but, you know, whatever logs going by, and I guess you could, like, fiddle with settings or whatever.
[1712.4s] But, yeah, all of that was in web three umbrella.
[1717.4s] That's a lot .
[1717.4s] That that was a lot .
[1717.4s] And all of the depend they were all really code oh, test and the test as well .
[1717.4s] Right ?
[1717.4s] Right .
[1717.4s] Right .
[1717.4s] Right .
[1717.4s] But then they were all really codependent.
[1726.8s] I mean, when I started, one of the first things I did was, like, what are the dependencies on all of these ?
[1726.8s] And it's like, what is all of this stuff?
[1733.9s] Because you had, like, libraries with it as well .
[1733.9s] It's like, Lib Ethereum, Lib
[1738.3s] web web three base.

**SPEAKER_00:**
[1741.6s] Yeah.
[1742.9s] Dev p two p .
[1742.9s] Live p two p .
[1742.9s] There were certain

**SPEAKER_01:**
[1747.1s] documentation all over the place .
[1747.1s] I mean You know ?
[1747.1s] I think, you know, I think what had happened there that Gab was sort of trying to do, but it never came to fruition and then he left, was it's like, right .
[1747.1s] Let's try and make this modular .
[1747.1s] Right .
[1747.1s] We're we're gonna try and do a modular thing and pull apart the networking and the database and this and the other.
[1766.7s] But it was it was pulled apart
[1769.4s] into separate repos before there were actually stable interfaces between any of these.
[1775.2s] So you had to use the latest stuff of anything anyway .
[1775.2s] Like, you couldn't mix and match because there was no versioning .
[1775.2s] There was no
[1781.4s] interplace discipline on any of it.
[1784.5s] You had to use all the latest ones together, but then it was all split into separate repos .
[1784.5s] So it's like, right .
[1784.5s] You're making a change on one of them and then whatever updating the sub modules and, like
[1795.7s] like, that wasn't atomic .
[1795.7s] It was it was just a big old mess.
[1801.0s] So, yeah, one of the first things I did was, like, you know, work out infer infer a dependency diagram,
[1808.6s] map a path to pulling it all back into a into a monolithic workspace,
[1815.7s] doing, like, automated builds that we somehow didn't have,
[1821.1s] and specifically
[1822.6s] decoupling
[1824.2s] and
[1825.2s] the tests from the client .
[1825.2s] Right ?
[1825.2s] Right.
[1829.5s] So
[1830.3s] for,
[1831.2s] for example, because it was tied in with this full workspace,
[1834.1s] it was literally a twenty four hour build.
[1836.9s] It was like compiling
[1838.8s] Chromium
[1839.6s] from source twice,
[1842.0s] compiling
[1842.9s] QT,
[1845.0s] all of this stuff .
[1845.0s] So
[1846.8s] just to get you know ?
[1846.8s] And and there weren't binaries available
[1850.7s] for Solsea either.
[1852.3s] Like, you had to build all of this stuff yourself to be able to, like, compile,
[1857.0s] you know, a smart contract to do anything .
[1857.0s] You have to do all of that.
[1860.8s] So I remember,
[1862.1s] you know, after all that decomposition,
[1865.3s] I, you know, I got it so you could just do.
[1869.4s] And, you know, that was a quick build.
[1871.9s] And then I did, like, homebrew,
[1874.8s] and it's like so you could do, like, brew install salsa, and they did it in, like, five seconds .
[1874.8s] And everyone's like, oh my god .
[1874.8s] This is not great .
[1874.8s] It was my benefit .
[1874.8s] It's amazing.
[1887.6s] But, yeah, it was,
[1889.4s] yeah, it was a bit of a mess .
[1889.4s] I I do remember waiting, like,

**SPEAKER_02:**
[1894.2s] you know, many times trying to build things, coming back,
[1897.7s] looking at it, saying, like, this can't be like, my machine's gotta be broken because, like, it can't be this long .
[1897.7s] Can't be, like, eight hours .
[1897.7s] Like, nothing I could imagine would take more than eight hours to do, you know, but you're right .
[1897.7s] It's just like

**SPEAKER_01:**
[1912.0s] You know, talking about that, you know, creative brew of lots of different people and uncoordinated
[1917.3s] and everything, One of my first observations on joining the the foundation is
[1923.2s] these people seem allergic to professionalism
[1927.0s] because that seems,
[1928.5s] you know, in an organized way .
[1928.5s] Well, you're one of the baddies .
[1928.5s] You know, you're the status quo .
[1928.5s] You're trying to subvert and take it over.
[1935.6s] You know, things as simple as, like like, you know, have we got, like, technical
[1940.2s] leads that actually lead?
[1942.0s] You know, have have we got any project management ?
[1942.0s] Have we got any IT ?
[1942.0s] Have we got
[1946.8s] anything?
[1947.6s] And it's like, no .
[1947.6s] It's just like a jumble of people doing stuff.
[1952.0s] And
[1953.6s] it's like, oh, how how on earth can you develop software in such a chaotic environment?
[1959.4s] But that was kind of the vibe as well .
[1959.4s] That was seen as a good thing,
[1965.7s] you know, because it's because that's a defensive cultural thing .
[1965.7s] Right ?
[1965.7s] You know, we don't we don't want this to be a Silicon Valley thing.

**SPEAKER_00:**
[1975.4s] Yeah .
[1975.4s] You know, I I
[1977.6s] think I
[1979.0s] just have a comment .
[1979.0s] It it's interesting, and maybe I commented on this in one of the other videos .
[1979.0s] One of these rare
[1985.6s] big software projects that did not very much come from The United States .
[1985.6s] It's Canada.
[1991.6s] It's different parts of Europe.
[1993.5s] You know ?
[1993.5s] And one of those confusing things, Bob, to your point about who got paid for the clients on the foundation, I think, like, I remember there being a deal struck with Zug,
[2004.3s] the the, you know, the the Canton basically around it .
[2004.3s] They were like, there's tax
[2010.2s] stuff and all that sort of thing, but they also sort of intended to hire and operate locally.
[2015.5s] They would either move there or they'd hire
[2018.2s] ETH Zurich grads or whatever.
[2021.7s] And I don't know the the the details specifically, but I think that didn't quite end up happening that way in
[2026.9s] sort of as a surprise.
[2028.7s] And I saw some of this firsthand at the meeting in which,
[2033.0s] you know, and Charles
[2034.6s] were were, you know,
[2036.7s] sent on their way.
[2039.6s] The the client team set up in their own countries,
[2043.1s] and that was, like, a bit of a flip.
[2045.6s] Like, Gavin wanted to be in Berlin because the
[2049.0s] I guess the devs were good and expensive, and they'd be, like, living there .
[2049.0s] You know?
[2053.6s] Inexpensive .
[2053.6s] Excuse me.
[2056.5s] And,
[2057.7s] yeah, I think it's just
[2059.6s] you know, you would running my own business, you would never make such a decision in such a flipped manner where, like, overnight, we're like, oh, we're in a different country .
[2059.6s] You know ?
[2059.6s] But they that was kind of a regular
[2070.2s] occurrence to some extent.
[2072.3s] Major
[2073.2s] things changing,
[2075.0s] you know, as part of how the the foundation plus
[2078.7s] sort of operated that that I saw .
[2078.7s] And, again, it didn't seem to hurt,
[2083.4s] you know, quite as much as you might expect.
[2087.2s] But yeah .
[2087.2s] But I think,
[2089.3s] you know, you you had to have you were lucky in how people works how excited people were about the project that that survived all of this.
[2098.1s] And, again, from our side, you know, we're sitting in the Bay Area at that time, and we're like, why why do they keep doing all of these things ?
[2098.1s] Like,
[2104.7s] they're they're trying to build a thousand things, and it's hard to build one thing.

**SPEAKER_01:**
[2109.7s] Yeah .
[2109.7s] I mean, you have so there there were separate legal entities for those as well .
[2109.7s] Right ?
[2109.7s] So you have f dev AG
[2116.3s] in in in Berlin,
[2118.1s] and then, you know, there was then there was an Amsterdam thing
[2122.2s] for for the Geth team .
[2122.2s] You had the London
[2124.6s] stuff as well, which was mainly communications
[2128.1s] sort of stuff,
[2130.0s] you know, with with Stefan and George Hallum,
[2134.0s] Ian,
[2137.2s] one other person who I forget.
[2141.7s] But, you know, you sort of talk about,
[2144.1s] you know, these people working for the Ethereum Foundation,
[2147.1s] like but it's it was always woolly than that .
[2147.1s] So, yeah, you did have the the the
[2153.2s] in in Zug,
[2156.7s] but most people, even if they're working full time, they weren't actually working for that .
[2156.7s] You know ?
[2156.7s] So when I had my contract, it was with the the for profit
[2166.9s] in
[2167.9s] Berlin .
[2167.9s] That was who I was actually working for, and then they were funded by
[2172.6s] the foundation.
[2174.3s] And and in
[2175.7s] general, that was another big split that it was .
[2175.7s] Right ?
[2175.7s] Was the you got the foundation,
[2180.2s] but then you had that
[2181.9s] was, like,
[2183.2s] the kind of umbrella group for that that was leading essentially .
[2183.2s] So I think the the Amsterdam thing, like, rolled into Berlin .
[2183.2s] I think that was also left side.
[2195.7s] And that in itself was, you know, a huge item of conflict .
[2195.7s] I know,
[2201.2s] again, in Laura's book,
[2203.6s] I think Joe was talking about that, right, was was the kind of, like, wanted a big chunk of money.
[2209.5s] It's like, right, you know, the funds are there from the crowdsale now, so, you know, give them all to us .
[2209.5s] Right ?
[2209.5s] And it's like, I
[2217.6s] don't know that we wanna give you all the funds, like, you know,
[2221.2s] as you go, but that, you know, that was typical of that period .
[2221.2s] It's just
[2227.6s] a mess of complexity and interpersonal
[2230.9s] things and organizational
[2232.9s] complexity.
[2234.3s] And with that with that Swiss
[2236.8s] people thing, so my understanding on that
[2239.4s] was that was like a
[2241.5s] main motivation for, like, getting renting that
[2244.8s] spaceship building .
[2244.8s] Right?
[2246.8s] Was the intention was that there were gonna be a load of people there, but, like, maybe it was, I think, tests
[2252.5s] testing was one of the ones I heard was maybe a goal there .
[2252.5s] It's like, right .
[2252.5s] We're gonna get a load of Swiss people to to test things .
[2252.5s] And there's also, like,
[2262.0s] Mihai with his ideas,
[2264.3s] of
[2266.4s] these co working
[2267.9s] spacey things around the world.

**SPEAKER_02:**
[2271.9s] And
[2272.9s] and when and also to make it a little bit more willier, like, you know,
[2277.2s] same time like, very shortly, consensus emerged out of that too, and they were doing a bunch of work .
[2277.2s] You know, we were working you know, we were technically
[2285.2s] working under consensus for, you know, the first low parts of it too .
[2285.2s] And
[2289.6s] all of that was, like, in the mix, you know, like everywhere .
[2289.6s] So
[2294.2s] I want to jump ahead a bit because we have you as an ETC expert, and in our last one, we had a lot of questions around
[2303.6s] what we remembered from sloket and the DAO hack.
[2307.5s] So maybe you could walk us through that and,
[2310.2s] you know, how ETC emerged out of that .
[2310.2s] That part was
[2313.9s] a little bit vague to us because we didn't we didn't follow much on, you know, how those pieces all came together.

**SPEAKER_01:**
[2321.3s] Yeah .
[2321.3s] So, I mean,
[2325.9s] one of the
[2328.7s] groups or companies that came out of this kind of, like,
[2332.6s] shrinking of the foundation
[2334.8s] was that
[2336.2s] on that c plus plus team that got most of the cuts,
[2339.8s] a good chunk of those people went to just went straight to parity
[2344.1s] and just, like, carried on with our new client.
[2347.0s] But Christophe who
[2348.7s] had been working, leading that testing effort, who were just talking about those same tests,
[2353.9s] he
[2354.7s] and
[2356.5s] and Stefan who
[2358.1s] had been
[2359.4s] community communication
[2360.9s] communications
[2362.0s] leader, you know, that sort of thing, community stuff,
[2366.3s] and left Eris, who'd also been on c plus plus team .
[2366.3s] Those three
[2370.8s] went off and formed a company called Slockit.
[2373.4s] So Slockit being smart locks,
[2377.2s] just the idea that you,
[2379.6s] you know, whatever if you're doing an Airbnb or something that you can,
[2383.5s] you know, that you can have a smart lock and that you could go and do your contract with someone for for the rental, and then that could be, you know, enabling
[2392.8s] something on the lock that's checking a
[2395.5s] an oracle or an on chain thing and and and so on.
[2400.2s] And
[2401.2s] so that that was the the that that product area.
[2405.6s] At DevCon one,
[2408.6s] they did, an on stage demo that was it was like a pot of it was like a pebble, like a pot .
[2408.6s] Yeah .
[2408.6s] I remember that .
[2408.6s] It's like doing a transaction that turned it on to make a cup of tea .
[2408.6s] Yeah .
[2408.6s] Like, that that was the the on stage demo.
[2425.2s] But
[2426.3s] what seemed to happen there was, like, they didn't wanna do an ICO.
[2431.5s] They wanted it to be
[2434.1s] fairer, I guess,
[2435.9s] because around that era,
[2438.3s] the more later, you know, you you saw lots of cash grab ICOs, and it's like, right .
[2438.3s] Here's all the money up front .
[2438.3s] You know, we're not gonna live it .
[2438.3s] What are you gonna do ?
[2438.3s] Right.
[2448.1s] So so they didn't wanna do that, you know, because they were very genuine people who come out of the foundation and were, you know, kind of, you know, ideologically driven.
[2457.6s] So
[2460.5s] Vitalik had written stuff about DAOs .
[2460.5s] Right ?
[2460.5s] You know,
[2464.2s] I think they were mentioned in the white paper even.
[2468.7s] And it's like, well, maybe we can make a DAO.
[2472.2s] So
[2473.7s] and I think that was just Slock It DAO, really, originally, and it was like, right .
[2473.7s] We're gonna have a DAO.
[2480.4s] The money is gonna go into there,
[2482.7s] but then it's only gonna get released to us as we deliver milestones.
[2487.8s] So it's kind of like this separation of, like, right, the DAO is where the money is,
[2492.4s] and that's controlled by the token holders.
[2495.5s] Slock it as a company, as a service provider into that,
[2499.9s] but we're a stackable service provider,
[2502.7s] and we're only gonna get paid as we go through the milestones .
[2502.7s] So it's like, oh, you know, that's really interesting .
[2502.7s] Yeah.
[2509.2s] And I to my understanding, that's what was presented at DEFCON one
[2514.1s] Okay .
[2514.1s] I remember.
[2515.8s] It was like, hey .
[2515.8s] We'll lock it .
[2515.8s] This is what we're doing, and we're gonna do it down with it .
[2515.8s] And it's like, oh, cool.
[2521.5s] But then they kept working on that that DAO
[2525.6s] stuff after DevCon one, and it just seemed to, like, warp into
[2530.8s] what we've made, like, a DAO framework.
[2532.9s] It's a DAO library,
[2534.7s] you know, because we want other people to be able to do this as well.
[2538.4s] But then that sort of turned into, well, actually,
[2541.9s] how about it isn't just us ?
[2541.9s] How about it could be anything ?
[2541.9s] Like, anyone could have a service provider .
[2541.9s] You could propose any anything into it, and then it became the DAO.

**SPEAKER_02:**
[2552.3s] Okay.

**SPEAKER_01:**
[2554.5s] And it wasn't capped.
[2557.1s] There was no cap on the contributions into it.
[2561.6s] There was really nothing else that you could do on Ethereum at that point .
[2561.6s] It was kind of like the first application,
[2567.4s] really.
[2568.7s] Well, I mean, you did have a two a few .
[2568.7s] You have this
[2572.0s] this gold thing.
[2574.2s] You did have
[2576.1s] die,
[2577.6s] think, was sort of coming to life just about at that point, but the DAO was kind of like the first big thing .
[2577.6s] Right .
[2577.6s] And it just sort of snowballed and snowballed .
[2577.6s] Right ?
[2577.6s] Because it's like
[2589.2s] there was it was also touted as zero risk
[2592.8s] because you could exit with your funds .
[2592.8s] Right ?
[2592.8s] If you didn't like the result of what was happening, you could just exit and have your f back .
[2592.8s] So it's kind of like, this is risk free .
[2592.8s] Right ?
[2592.8s] It's like a risk you know, it's like a sovereign bond or whatever .
[2592.8s] Right ?
[2592.8s] Right .
[2592.8s] There's no downside here .
[2592.8s] This is risk free.
[2607.6s] Though tons of people are like, well, what else am I gonna do ?
[2607.6s] I'm just sitting here on me for I can't do anything .
[2607.6s] Well, you know, pile on in.
[2615.0s] And
[2615.8s] the Ethereum crowdsale
[2617.7s] raised, what, is 16,000,000,
[2620.0s] I think, in Bitcoin,
[2622.2s] which was
[2623.5s] I think it was number
[2625.2s] five crowdsale of all time .
[2625.2s] You know ?
[2625.2s] Was, like, comparing to Kickstarter projects.
[2629.8s] Right .
[2629.8s] So it's like, you know, maybe the Dow will do, you know, 2 or 3,000,000, maybe five,
[2636.4s] and it just went
[2639.8s] until it was, you know, it was just absolutely gigantic.
[2645.3s] And I remember at the time thinking, you know, this is
[2649.2s] I don't like this .
[2649.2s] Like, DAO, it's not this is not a good idea.

**SPEAKER_02:**
[2653.5s] Yeah .
[2653.5s] And

**SPEAKER_01:**
[2654.9s] and the main reason I was thinking of that was,
[2659.6s] is this a security?
[2661.2s] Right .
[2661.2s] Is this
[2663.6s] seen as, you know, money transfer
[2666.7s] stuff
[2668.6s] because you've got slot at the company,
[2671.0s] and then they have this thing called DAO link
[2673.8s] that was
[2675.0s] sort of a service company for
[2677.6s] paying people in
[2679.0s] real life .
[2679.0s] It was that was some
[2681.2s] at Swiss thing, I think, or or what's Bitcoin Swiss?
[2685.6s] And then you have the DAO itself.
[2688.0s] You have the curators as well.
[2690.7s] So anyone could could propose,
[2693.2s] you know, a smart contract that encoded their proposal .
[2693.2s] Right ?
[2693.2s] They they would make a written description of the thing, and here's a smart contract doing it.
[2703.9s] And the curator's
[2705.2s] role was, like, to verify,
[2708.1s] yeah, what they've sort of said
[2710.3s] in text is kind of what they've done .
[2710.3s] It was meant to be like, you know, this kind of administrative
[2716.3s] role.
[2717.7s] But what happened is all of those guys, that was their name their names and faces up on the website.
[2723.3s] You know ?
[2723.3s] So, like, DAO hub website
[2726.0s] is just like a who's who of the Ethereum Foundation, basically .
[2726.0s] Right.
[2730.4s] And it didn't say,
[2732.0s] you know, Christian creator
[2734.9s] of Solidity.
[2736.3s] It said,
[2737.8s] Ethereum
[2739.1s] Foundation, Vitalik, Ethereum Foundation.
[2742.0s] You know ?
[2742.0s] So lots of people were like, this is an Ethereum Foundation project .
[2742.0s] Right ?
[2742.0s] Because you you've all got your names on everything.
[2748.9s] So I thought there was firstly, there was huge, like, legal liability on those guys
[2753.8s] because where Slockit got these layers of legal protection, these guys haven't .
[2753.8s] They're just doing it as individuals.
[2759.0s] Right.
[2759.8s] And I remember Fabian
[2763.7s] talking to me and talking
[2765.5s] to the group in the foundation .
[2765.5s] It's like, you know, I've been talking to some of my friends, and they're like,
[2770.6s] you know, they don't think this is a great idea, and I'm thinking of talking to a lawyer and
[2775.1s] a gav back town .
[2775.1s] Right?
[2778.4s] A a couple of weeks before the
[2781.3s] disaster,
[2782.2s] Gav just backed out .
[2782.2s] He's like, you know, this is,
[2785.6s] you know, this this is not what I signed up for .
[2785.6s] I thought it was just a small role, and now it's, like,
[2792.3s] presented as a lot more and you know ?
[2792.3s] So he he backed out.
[2798.2s] A lot of the others didn't
[2800.0s] because because it was like, well, if we back out, it's gonna, like, ruin it, and it's like a great experiment.
[2806.5s] But I thought there was huge liability to them .
[2806.5s] I thought there were legal risks.
[2810.9s] And I also just thought it was a stupid idea.
[2813.6s] Like, why would you have thousands of random people putting their money in a bucket and then let's, like, vote on what to do with it ?
[2813.6s] Right .
[2813.6s] Who who are these people ?
[2813.6s] Like, what do they even know, like, about a business proposal or anything?
[2827.2s] It's just like, this is a stupid idea,
[2830.2s] but, you know, I didn't have my eye on the fact that all of the tech stack was incredibly immature at that point .
[2830.2s] Right ?
[2830.2s] Yeah.
[2837.5s] There's no best practices .
[2837.5s] There's no libraries.
[2840.3s] It's just here's some code.
[2843.2s] And and they just went all in .
[2843.2s] Right ?
[2843.2s] It was like code is law .
[2843.2s] Yeah .
[2843.2s] Contract you know, the smart contract is the contract.
[2849.7s] You know ?
[2849.7s] YOLO, you can't stop us.
[2852.6s] Kaboom.

**SPEAKER_02:**
[2854.0s] But
[2856.0s] but okay.
[2857.2s] And then the hack happens .
[2857.2s] Right ?
[2857.2s] And and I remember the details of the hack being they found a flaw in the smart contract code,
[2865.7s] and they could basically withdraw those funds
[2869.1s] into another account.
[2871.1s] And Yep .
[2871.1s] I remember there was some kind of race between, like, the people at
[2877.0s] the DAO slash Locket who are, like, using the same exploit to, like, drain
[2882.8s] the account, like,
[2884.4s] using the same hack, basically .
[2884.4s] Is that right ?
[2884.4s] Yeah .
[2884.4s] So there was this reentrancy bug

**SPEAKER_01:**
[2891.1s] where
[2892.7s] it it's really sort of, like, to do with
[2896.1s] atomic operations or order of operations.
[2899.7s] So your your reentrancy
[2901.8s] was that you could be calling
[2904.8s] because people were supplying, like, their proposals, and it's like, hey .
[2904.8s] Here's a smart contract that's implementing mine .
[2904.8s] You were, like, calling into their code, but you can't know what theirs is gonna do .
[2904.8s] Mhmm .
[2904.8s] So there was this reentrance issue where within that
[2919.0s] other person supplied code, you could, like, kind of call back in, and it was sort of like
[2924.3s] so it was to do with child DAOs.
[2926.6s] So this whole zero risk thing
[2929.0s] was like, if you didn't like proposals that were happening,
[2932.6s] you could make a child DAO of saying, well, hey .
[2932.6s] I'm I'm out .
[2932.6s] Right ?
[2932.6s] I'm taking my and my voting off into this other one .
[2932.6s] Right ?
[2932.6s] I'm not I'm not following you .
[2932.6s] I'm I'm going there.
[2944.2s] Another people could join you as well .
[2944.2s] So I guess the idea was like, right .
[2944.2s] You know, here, we've got this totally over general DAO, but we're gonna make a, you know, like a DeFi DAO or an NFT DAO or whatever.
[2956.9s] Right ?
[2956.9s] And and it's like,
[2959.3s] I guess, little bit like some of the thoughts for for consensus and hub and spoke is like, you know, you're gonna get this universe of stuff just flourishing out and
[2968.7s] childs and and and so on.
[2971.5s] But, yeah, the problem on that on that child down thing is that there was this reentrancy bug where rather than just being able to pull
[2979.5s] your f or your share,
[2981.9s] you can actually go in and pull more and more .
[2981.9s] So you have this using
[2986.0s] this and a child down and pulling a giant amount of of of the funds into that
[2992.7s] child down.
[2994.1s] And then within thirty days, they'd be able to exit with the funds.
[2998.7s] But but kind of the
[3002.0s] the blessings, I guess, of that setup is they're not immediately exiting with the funds .
[3002.0s] Right ?
[3002.0s] They haven't gone already and sold it on an exchange, they're done before you notice .
[3002.0s] You have got this period.
[3013.6s] And then the other thing is that you could join them.
[3016.3s] You can go into the child DAO as well .
[3016.3s] So after the hack,
[3020.3s] you know, there was this appeal out .
[3020.3s] Hey .
[3020.3s] You know, did did anyone participate in this,
[3026.1s] you know, specific child DAO ?
[3026.1s] Was anyone in there ?
[3026.1s] And it's like, yeah .
[3026.1s] You know ?
[3026.1s] Yeah .
[3026.1s] Somebody else is in there .
[3026.1s] And then what you could do is you could,
[3033.2s] you know, you could child DAO again .
[3033.2s] It's like you could do it another one .
[3033.2s] It's like, like, what what I'm gonna grab it off you, and you're gonna grab it off me .
[3033.2s] And
[3042.2s] so, you know, you could have had this this DAO wars thing of of, like, you can never stop it, but you could delay it indefinitely.
[3050.0s] So that was one of them.
[3051.6s] But then the other white hat thing is, like, okay .
[3051.6s] Well, we know about the bug,
[3056.2s] so we can do it too .
[3056.2s] You can have white hat people like, well, we're gonna seal all of the money out of the top out of the top DAO as well,
[3063.8s] but we're doing it for good .
[3063.8s] Right ?
[3063.8s] We're we're we're doing it here to keep it, to give it back .
[3063.8s] Right.
[3069.4s] So so, yeah, you had all of those games going on within that existing setup.
[3075.1s] But then as a reaction to that, you had all of this discussion about, well, you know, are we gonna react ?
[3075.1s] Are we not gonna react?
[3082.4s] First
[3083.2s] the first proposal was a was a soft walk,
[3087.2s] but, you know, it was just gonna, like, blacklist out
[3091.4s] stuff to do with the with the hacker .
[3091.4s] Right ?
[3091.4s] And they did do that soft fork .
[3091.4s] Right ?
[3091.4s] I remember they did that soft fork first, and then they did done for it, and I think it might even have gone on test nets and things, but it never went live .
[3091.4s] Okay.
[3105.8s] Because it was spotted that it was a denial of service attack.
[3109.5s] Got it .
[3109.5s] Because that blacklisting
[3112.1s] was, like,
[3114.5s] you know, not accounted for in the cryptoeconomics.
[3117.1s] So it was like,
[3119.1s] yeah .
[3119.1s] Yeah .
[3119.1s] You you you had a denial of service attack
[3123.4s] thing on that soft fork.
[3125.4s] So it got done, and then it got undone.
[3129.1s] And then the hard fork was like, okay .
[3129.1s] Well,
[3132.2s] we can we can go in and we can do an irregular
[3136.2s] state transaction
[3138.7s] where at a certain block,
[3141.5s] you know, you're just gonna have a hard coded thing
[3144.3s] which
[3145.2s] sticks
[3146.3s] different
[3148.4s] bytecode
[3149.6s] into
[3151.1s] into the address of the of the DAO,
[3154.1s] which is like, okay .
[3154.1s] Yeah .
[3154.1s] That thing,
[3157.2s] it didn't happen.
[3159.9s] You know, what's actually at that address is a simple refund thing where you can all get your money back.
[3166.7s] So so that's that was the our hard fork.
[3170.0s] Okay .
[3170.0s] And that's

**SPEAKER_00:**
[3172.6s] I just wanted to ask, where were you at this time ?
[3172.6s] Because I know you got involved,
[3177.0s] I believe, later with ETC because it didn't exist yet .
[3177.0s] And
[3181.3s] so,
[3182.6s] you know, how in terms of your personal perspective on all this, we're actually implementing
[3187.2s] anything
[3189.9s] yourself because, obviously, you've got pretty deep knowledge of the technical
[3194.2s] internals.

**SPEAKER_01:**
[3196.5s] Yes .
[3196.5s] What what are you doing ?
[3196.5s] I was I was working for the foundation .
[3196.5s] I was on c plus plus team at that point .
[3196.5s] I you know, this is about
[3204.6s] three or four months after I I'd started.
[3208.3s] The thing that was really interesting to me was
[3213.5s] how different people's
[3215.7s] thoughts or perspectives were
[3218.2s] even within the foundation.
[3220.1s] You know ?
[3220.1s] That you'd have people,
[3223.4s] say, working on gas
[3225.7s] going, well, of course, we shouldn't do anything.
[3228.9s] Well, of course, we should .
[3228.9s] And it's like, you know, been working with you for a year .
[3228.9s] Like, what ?
[3228.9s] What ?
[3228.9s] You think that ?
[3228.9s] Like, woah .
[3228.9s] You know, you have this real mixture of of reactions.
[3242.5s] And, I mean, my my first reaction was, well, you know, of course, you don't
[3246.8s] do anything .
[3246.8s] Like, it's an immutable blockchain .
[3246.8s] That's the whole point .
[3246.8s] Like, you know,
[3251.9s] you don't like the outcome .
[3251.9s] Well, you know, tough titties.
[3255.8s] You know, you you saw you've seen so many,
[3258.9s] you know, like,
[3260.0s] You know, you didn't have the Bitcoiners going all that .
[3260.0s] You know, let's let's, you know, let's try and fix this up or
[3267.6s] you know ?
[3267.6s] And I think
[3270.1s] the only reason it happened was because of the scale of it, you know, that it was a significant
[3274.9s] chunk
[3276.1s] of the entire
[3278.1s] ETH
[3279.4s] money money base.
[3283.1s] And, also, I I think that, you know, things weren't
[3287.6s] super great on funding and,
[3290.5s] you know, it wasn't like Ethereum was sure to succeed .
[3290.5s] It was quite, you know, nascent at that point .
[3290.5s] Yeah .
[3290.5s] And I know that there were also worries about
[3300.9s] the proof of stake transition and the fact that if you had a large amount of of the in,
[3308.1s] you know,
[3309.8s] hostile hands
[3311.8s] that you could maybe have years of, like, greeting attacks and
[3317.1s] stuff like that.
[3319.8s] But, also, I think there was just you know, a lot of people were like, well,
[3324.0s] you know, this is theft .
[3324.0s] Right ?
[3324.0s] You know, that money was intended for building the ecosystem, and, you know, some guys come in and stolen it .
[3324.0s] And
[3332.8s] if we can fix that, well, we should.
[3336.9s] So so yeah .
[3336.9s] I mean, I
[3340.1s] you know, my immediate reaction was you shouldn't, but I I also it was like, well, you know, whatever .
[3340.1s] That seems to be the consensus that we do it, you know, and
[3349.7s] okay.
[3350.6s] Off off, you know, off we go.
[3354.3s] Though I wasn't at the foundation many more months after that anyway, but,
[3359.3s] you know, there there was this real
[3361.9s] schism.
[3363.4s] Though I think from what I saw, I I think probably about 85%
[3367.4s] of people wanted to do the hard fork and 15 didn't
[3371.2s] or maybe eighty twenty .
[3371.2s] But I think I think there was pretty strong
[3375.1s] consensus to to to to do it,
[3378.4s] but that was,
[3379.9s] you know, very contentious
[3382.3s] for,
[3383.2s] you know, a not
[3385.1s] tiny group of people.
[3387.8s] You know, that a a lot of people that had got involved with Ethereum have done so because they they kinda wanted smart you know, Bitcoin with smart contracts.
[3397.4s] And and if you're about bitcoin y mindset, then, you know, like, of course, you don't, you know, don't screw with things.
[3405.1s] But but I think there's also this larger group
[3408.4s] that were like, well, ether isn't money anyway.
[3411.8s] Like, that was a messaging that had been given out at the time .
[3411.8s] It's like, no .
[3411.8s] No .
[3411.8s] It's fuel .
[3411.8s] Right ?
[3411.8s] It's fuel for the engine.
[3418.1s] Though, I think part of that is just, like, trying to dodge legal liability.
[3422.5s] But but, you know, that was also true as well .
[3422.5s] You know, this whole world computer,
[3427.7s] you know, here's a platform .
[3427.7s] Right ?
[3427.7s] You know, it's a platform like the web or Android.
[3432.2s] So I think it was sort of like that that was the mental split .
[3432.2s] It's like,
[3436.7s] is it money?
[3437.9s] And if it's money, you don't move people's monies without private keys .
[3437.9s] Like, you know, that's that's a mortal sin.
[3444.5s] And on the other side, you're like, well, no .
[3444.5s] It's a bug .
[3444.5s] Right ?
[3444.5s] It's a bug in the platform.
[3448.7s] And it's like, well but it's but it was a bug in the smart contract .
[3448.7s] Well, you know, if you've worked on serious software projects, you know, people hack shit on the wrong layers all the time .
[3448.7s] Right .
[3448.7s] Because it's gonna give you a better user experience .
[3448.7s] Like, you know, you don't have to be,
[3463.0s] you know, pure
[3464.3s] on that .
[3464.3s] It's really about how the thing works .
[3464.3s] So, you know, you get hacks in the wrong layers all the time.
[3472.5s] And if if you're just seeing it as a as a software platform, then, yeah, it's a bug .
[3472.5s] You fix the bug.

**SPEAKER_02:**
[3478.8s] So it's rare in life that you can actually see a counterfactual,
[3482.9s] but in this case,
[3484.3s] we can because
[3485.8s] ETC was created at that time and kind of emerged out of that .
[3485.8s] So, like,
[3492.2s] you know, can you talk a little bit about that, and how has that gone ?
[3492.2s] Because you're deep into that ecosystem,
[3497.1s] obviously, as the, you know, director of the Ethereum Classic Cooperative .
[3497.1s] Like,
[3501.9s] how does it work now ?
[3501.9s] Like, you know, what how did those words divide?
[3506.5s] And
[3507.7s] then, you know, how are those words continuing?

**SPEAKER_01:**
[3511.0s] So over that month or so, right,
[3514.2s] where it's like, you know, the money's been stolen into the sub down, but we're gonna do anything .
[3514.2s] You know, you have the most,
[3521.6s] you know, vigorous debate on all platforms .
[3521.6s] Right ?
[3521.6s] You know, it was the the topic .
[3521.6s] You know, what's gonna happen ?
[3521.6s] How's it gonna go and everything .
[3521.6s] Right ?
[3521.6s] So, you know, I don't think there's anyone that was, like, unaware of this stuff happening .
[3521.6s] You know, it's very, very everyone with their eyes open.
[3538.6s] But, yeah, you know, you just you just have this group of people kinda gathering together,
[3543.5s] and it's like, no .
[3543.5s] We're, you know, we're not gonna go with it .
[3543.5s] This is not gonna happen .
[3543.5s] Or or at least, like, you know, we're not following the hard fall .
[3543.5s] Maybe people do, but, you know, a bunch of people deciding not to.
[3555.6s] The other thing I thought was really interesting at the time and was to my mind the the best thing of all about that chain split
[3563.3s] is to that point,
[3565.3s] I don't think there'd ever been a minority chain that survived.
[3569.6s] Right ?
[3569.6s] The the standard thinking is, like, you're gonna have a winning side and a losing side.
[3575.0s] And, you know, that it's gonna happen, and we'll see where where's the thing you know, where are the people going,
[3580.6s] which is the winner and then the losers .
[3580.6s] You know ?
[3580.6s] Well, you know, like, people will stop mining .
[3580.6s] It will just die .
[3580.6s] Right ?
[3580.6s] Because it's the loser chain .
[3580.6s] So
[3588.1s] there's no economic value there and, you know, forget it.
[3591.6s] But what actually happened on the ATC side is, you know, you had miners that were like, well, you know, just gonna keep on mining .
[3591.6s] I'm not updating, you know,
[3600.1s] you know, some of it going, you know, the evil Ethereum Foundation and, you know, the talent's a dictator.
[3605.6s] You know ?
[3605.6s] I mean, I don't think any of that's true.
[3609.1s] But you had got people that were like, no .
[3609.1s] I'm gonna keep going .
[3609.1s] And then, oh, look .
[3609.1s] Block production's still going, and, you know, it's still happening there.
[3617.5s] And then listed
[3619.1s] it, and then it's got a market value, and then you've got speculative activity around that.
[3624.3s] You've got ether holders, like, dumping their ETC, you know, it's, hey .
[3624.3s] It's free money.
[3630.1s] But also, you've got other people on the other side going, well, you know, I see real value here and, like, this ETC is going cheap.
[3637.5s] So, you know, noticeably
[3639.5s] notably,
[3640.7s] Barry Silver,
[3642.4s] who
[3644.3s] first
[3645.6s] non
[3646.4s] Yep .
[3646.4s] In Ethereum to that point,
[3650.1s] presumably, like, based on pre mine and various
[3653.5s] other things, but was like, well, oh, actually, like, you know, an immutability focused ETC,
[3660.3s] you know, would be would be really interesting.
[3663.3s] So, yeah, you just got this sort of grassroots thing forming.
[3667.5s] You got volunteers
[3668.7s] jumping up saying, hey .
[3668.7s] You know, I'm a developer .
[3668.7s] I'll keep maintaining the the classic Geth clients and so on .
[3668.7s] And,
[3676.4s] you know, and it it it found its own
[3680.9s] legs that, you know, you had, like, the the Ethereum subreddit was, like, a primary communication platform at that point, and then you had, like, an Ethereum classic one,
[3690.4s] you know, being created and some people in,
[3693.4s] you know, one side, some on the other .
[3693.4s] But, you know, it got quite bitter in the end .
[3693.4s] Right ?
[3693.4s] You know, you've got a lot of people that were like, you know, foundation.
[3700.8s] You guys either just ruined.
[3703.2s] Yeah .
[3703.2s] You've just ruined the project,
[3706.7s] and you had people
[3709.2s] on the other side seeing is seeing ETC is really illegitimate,
[3713.5s] you know, as as saying, well, look, you you know, it's just a money grab .
[3713.5s] You just want your free money.
[3718.8s] You know ?
[3718.8s] Why are these Bitcoiners kinda coming over ?
[3718.8s] Like, they weren't interested in Ethereum before, and now they are .
[3718.8s] Like, that's not, you know,
[3726.2s] you know, that's that's not good .
[3726.2s] And and you did obviously have a bunch of speculators in there as well, so that's sort of a bit nasty too.
[3734.4s] But I think the thing that, like, set up those communities
[3739.1s] finally was this, like, 100% f meme,
[3744.5s] which came about because
[3746.6s] somebody
[3747.6s] tweeted,
[3749.7s] hey, metallic .
[3749.7s] I hear that you're working on ethereum classic .
[3749.7s] Is there any truth to this?
[3754.8s] And he said, no.
[3757.7s] You know, I'm I'm only working on ethereum.
[3761.5s] And
[3762.3s] the person then said, well, what if ETC had more market cap than Ethereum?
[3767.3s] And he said, no .
[3767.3s] I still wouldn't work on it a 100% half.
[3772.4s] Like, he wasn't saying it in a purity pledge way .
[3772.4s] He he was just in the way he does being just making a factual statement.
[3780.9s] But then I remembered, you know, Joe replied, you know, I'm a 100% half .
[3780.9s] And then it it's like everyone's doing it .
[3780.9s] Right ?
[3780.9s] It's this purity pledge.
[3788.5s] You know ?
[3788.5s] Everyone is expected to, you know, pledge allegiance to ETH.
[3793.4s] So it became a, you know, oh, shit .
[3793.4s] Is this an either or ?
[3793.4s] Like, you can't be in both .
[3793.4s] Like, if you if you you're interested in ETC, then you, you know, you're a dirty person.
[3804.1s] So I think that that really
[3806.1s] wedged it, you know, wedged it permanently apart at that point.
[3810.5s] And and also, you know, a number of the people that were
[3814.3s] volunteering on ETC, you know, they were really angry.
[3817.2s] They were like, you know, well, I, you know, been involved for
[3821.2s] two two and a bit years in this project,
[3824.4s] you know, really pumped about everything that you can do with Ethereum, and then you guys have, you know, have wrecked it.
[3830.7s] So there was a lot of, you know, bitterness
[3834.3s] from that ETC side back.
[3838.1s] But then, you know,
[3839.6s] things kind of split apart, and
[3842.1s] and over time, ETC, you know, found its own path.
[3846.0s] So
[3847.2s] with the real differentiation
[3848.8s] being
[3850.4s] well, firstly, the DAO hack didn't happen .
[3850.4s] That was the only initial difference .
[3850.4s] Right .
[3850.4s] Very rapidly, though, there was this conclusion
[3858.4s] that fixed economic policy was needed .
[3858.4s] You know, the ETC was really like Bitcoin
[3864.3s] with Ethereum technology, but, you know, Bitcoin,
[3867.2s] you know, culture and and ethos.
[3869.6s] Right .
[3869.6s] So it's like, right .
[3869.6s] You know, there's
[3872.2s] no fixed monetary policy for for Ethereum .
[3872.2s] And, I mean, you see this over many years .
[3872.2s] There's, like, you know, change of change of block rewards,
[3880.3s] ice age, delays,
[3883.7s] fee burning,
[3884.7s] you know, many, many changes.
[3886.5s] So
[3888.1s] that was the first kind of, like,
[3890.8s] major change on the ETC side was introduction of that fixed monetary policy because there was consensus that that was import you know, that was, like, bad inheritance
[3899.2s] that we that we wanna fix.
[3901.2s] And the other thing that that enabled was the the grayscale
[3905.1s] ETC fund.
[3906.8s] So at that point, it's like, right .
[3906.8s] Okay .
[3906.8s] This is really a Bitcoin feeling thing, and,
[3912.7s] you know, there's a feeling that there's that there's value here .
[3912.7s] So then from from that, Grayscale then created
[3920.9s] the
[3921.7s] the EC cooperative that I work from.
[3924.5s] You know ?
[3924.5s] So a share of the fees went into that kind of
[3929.3s] not quite a foundation, but a bit like a foundation,
[3932.6s] you know, nonprofit to support the ecosystem.
[3936.7s] And then the other thing more recently is is just proof of work .
[3936.7s] You know, there was there was sort of fairly rapidly a consensus that
[3944.2s] he just wanted to stick with proof of work indefinitely,
[3947.1s] but that
[3948.2s] that
[3949.1s] proof of state was seen as a,
[3951.6s] you know, as a centralizing
[3955.6s] oligarchic
[3957.4s] kind of thing that that didn't really fit with that with that ethos.
[3962.3s] But more generally, ETC is tracking protocol changes in Ethereum, you know, very compatible.

**SPEAKER_02:**
[3968.8s] So there have been
[3970.3s] forks, but not the hard fork along the way because Although you need to So the yeah .
[3970.3s] I mean, they've

**SPEAKER_01:**
[3976.7s] hard forks, but not chain splits.

**SPEAKER_02:**
[3978.8s] Got it .
[3978.8s] Okay.

**SPEAKER_01:**
[3980.3s] In the in in the old protocol updates
[3983.0s] on Ethereum as well, you know, they're they're all hard forks,
[3986.6s] and the old side doesn't actually go away .
[3986.6s] You know ?
[3986.6s] You could run a you could run a frontier node if you wanted .
[3986.6s] You can mine on frontier, mine the Olympic test net, mine any of these ones .
[3986.6s] It's just it's just
[3998.7s] you have had the wither and die because there hasn't been contention.
[4002.8s] But on ETC,
[4004.7s] you have sufficient contention that you had a chain split.
[4009.5s] But, yeah, I
[4012.1s] guess that's a a a sort of a Bitcoin thing is saying, you know, forks are are bad.
[4017.7s] Right .
[4017.7s] But it's like
[4020.0s] conscientious hard forks are bad.
[4023.3s] Hard forks are an upgrade mechanism for the protocol.

**SPEAKER_03:**
[4026.9s] Got it .
[4026.9s] Yeah .
[4026.9s] I mean, I remember I I had to implement that fork a few years ago, and and it was pretty blatant .
[4026.9s] It was just like, take money from here and place it here.
[4037.3s] By the way, it didn't bug me.
[4039.1s] But but we had people in red block apps who who who thought of it as, like, a stab to the back .
[4039.1s] They were, like, so upset by it .
[4039.1s] So

**SPEAKER_01:**
[4047.0s] Well, I mean, it's literally here's an array of addresses, right, to fuck with.

**SPEAKER_03:**
[4051.2s] Yep .
[4051.2s] I remember that was I I I don't remember what else was in there, but I remember, like, the majority of it was just, like, take a bunch of money and put it into these addresses, and that was the that was the fork.

**SPEAKER_01:**
[4062.3s] Yeah .
[4062.3s] You know, for this list of addresses, replace
[4065.9s] you know, it was
[4067.6s] yeah.
[4068.6s] You know, replace the the bytecode with this other bytecode.
[4072.4s] And, also, yeah, move I I think the moving was consolidating the child down .
[4072.4s] So I think I think that's what that was doing .
[4072.4s] So it's like move the money from the child DAOs back into the parent DAO
[4083.4s] and change the bytecode.
[4086.5s] Like, I think, you know, if block equals this,
[4089.8s] do a horrible thing.

**SPEAKER_02:**
[4093.1s] But in in the equals this steal money .
[4093.1s] Go ahead .
[4093.1s] Yeah.
[4097.8s] In the ETC world where the Dell hack happened, are those funds ?
[4097.8s] Like, did the hacker pull out those funds ?
[4097.8s] Did okay .
[4097.8s] So, like

**SPEAKER_01:**
[4107.0s] Yeah .
[4107.0s] Yep.
[4108.5s] Interesting .
[4108.5s] Yeah .
[4108.5s] I mean, again, Laura has
[4110.8s] a great write up of all of this in her book, the Cryptopians,
[4115.0s] including
[4117.7s] working out who it probably was.

**SPEAKER_02:**
[4120.1s] Oh, wow .
[4120.1s] Okay .
[4120.1s] Wow .
[4120.1s] So

**SPEAKER_01:**
[4123.2s] she didn't name names in the book, but then she did a an article,
[4130.1s] like, on the release day or just before
[4132.9s] naming who she thinks it was .
[4132.9s] So that's an interesting story .
[4132.9s] I can I'll I'll dig out that article and
[4138.8s] send it to you guys so you can add it to the
[4141.8s] description here.

**SPEAKER_02:**
[4143.3s] Cool .
[4143.3s] And but, you know, Bob, you're a natural born bridge builder .
[4143.3s] As we said, you get along with everyone.
[4149.1s] Do you ever see the,
[4150.9s] you know,
[4154.0s] valley between Ethereum and Ethereum Classic
[4157.4s] narrowing or getting better, or do you think it is getting better?

**SPEAKER_01:**
[4164.5s] I mean, the the problem that Ethereum Classic has always had
[4168.4s] from the time of the split, and it comes back to money again.
[4171.7s] Like, I I think that was the one thing that the foundation
[4175.5s] did wrong.
[4178.7s] You know, like, not not talking about the developers or the decision on that or whatever
[4184.3s] was to only put the money on one side
[4189.0s] because what that did is disenfranchised
[4192.8s] a good chunk of people who had, you know, invested in the presale, who'd been part of that community, who'd genuinely been,
[4200.5s] you know, actively involved for those first two years,
[4205.0s] and they were just left in the dust .
[4205.0s] It's like, you know, fuck you guys .
[4205.0s] We don't care what you think .
[4205.0s] Goodbye .
[4205.0s] Right .
[4205.0s] You know ?
[4205.0s] And the trademark's going this way and all the funds are going this way
[4214.4s] and, you know, and all all the developers went that way as well .
[4214.4s] And, I mean, obviously, like, the foundation can control that, what people choose to work on.
[4223.1s] But what that meant is effectively
[4225.9s] that group of people got defunded.
[4229.3s] Like, totally done .
[4229.3s] You
[4231.7s] I'm sorry, my child .
[4231.7s] I I disavow you, and I'll kick you out of the house, you know, forever, and I wish I'll never talk to you again.
[4240.7s] You know, I think in retrospect,
[4242.4s] it should have been like,
[4244.4s] okay .
[4244.4s] Funding is available for that other fork as well .
[4244.4s] And you may hate us, you know, and not wanna talk to us, I, you know, I guess it's like, know, a child, you know, whatever teenager I'm acute and I'm leaving home .
[4244.4s] And it's like, okay .
[4244.4s] But I'm not gonna stop
[4259.3s] putting aside savings and money for you .
[4259.3s] I you know, you might not love me now, but, you know, I'm you're my child too, and, you know, we'll we'll find a way of making it happen.
[4269.1s] You know ?
[4269.1s] Because,
[4270.8s] say, with the EC Cooperative,
[4273.3s] you know, it could have been well, when that came into,
[4275.8s] you know, into existence,
[4278.0s] the foundation could have gone well .
[4278.0s] Okay .
[4278.0s] You know, like, here's a body that can help, and there you go .
[4278.0s] We we're gonna fund it as well.
[4285.3s] And that there was something a little tiny bit like that with Virgil.
[4290.2s] So Virgil was also a huge bridge builder between Ethereum and Ethereum Classic.
[4296.5s] So in 2018,
[4298.1s] he invited Anthony Boussardy,
[4300.3s] who was my predecessor,
[4301.9s] to speak at Adcon.
[4303.3s] So this was May 2018,
[4305.4s] and that was the first Ethereum Classic
[4308.2s] talk at an Ethereum event,
[4310.7s] you know, being nearly two years
[4313.2s] at that point.
[4314.9s] And, you know, and it was fine and it was cool and everyone was, you know, everyone was friendly and, you know, and various others came to that talk and,
[4323.7s] you know, it's all all kind of friendly.
[4327.2s] And
[4329.0s] and Anthony invited me
[4331.0s] to
[4331.8s] Ethereum Plastics Summit,
[4333.9s] which was in September 2018 .
[4333.9s] So myself and Virgil went and spoke at that event.
[4339.8s] And around that time, Virgil,
[4342.4s] they somehow they found some ETC
[4345.3s] that that the foundation still had .
[4345.3s] You know, generally, they did a market dump at that time,
[4352.1s] but there was some stuff that they found, you know, so it's like $50 or something like that .
[4352.1s] And so we got that donated to the co op, which was Great .
[4352.1s] That was a that was a really nice
[4363.2s] nice kind of thing.
[4365.7s] But, you know, it was kind of like, here's a little gesture.
[4369.5s] But, really, I think I think that was a that was a real failing because it was a legitimate,
[4376.5s] you know, irreconcilable
[4378.1s] difference.
[4380.0s] But but it was made even worse by this, you know, 100 f
[4385.1s] purity pledge
[4386.5s] combined again with
[4389.3s] all the money's gone.
[4390.8s] So you end up with, you know, a very small community of
[4394.7s] mainly people who are, you know, very ideologically
[4397.6s] outraged
[4399.4s] by it .
[4399.4s] You know ?
[4399.4s] If you've got speculative
[4403.1s] token holders,
[4405.1s] obviously, that, you know, they're gonna stick with Ethereum .
[4405.1s] You know, what's this other thing, this new thing, and there's nothing
[4410.7s] you know?
[4411.7s] So so that's always been the the issue that that ETCs
[4415.5s] had is,
[4417.7s] you know, lack of,
[4422.2s] you know, lack of lack of money and interest, really.
[4427.2s] More recently, we've had support from Bitmain.
[4430.8s] Mhmm .
[4430.8s] After the merge with Ethereum moving to proof of stake, all of a sudden, ETC is one of the larger
[4437.3s] mining
[4438.5s] ecosystems.
[4439.6s] So all of a sudden, we, you know, we're very aligned with with with Bitmain .
[4439.6s] You know, they wanna sell ASICs .
[4439.6s] They wanna be
[4446.0s] using Ampull for mining .
[4446.0s] So
[4448.7s] so they're supporting a grants program now.
[4451.6s] But, yeah, you know, ETC is you know, it it's small,
[4456.8s] but you have,
[4458.2s] you you know, you have some people, and that's, you know, that's their that's what they want.

**SPEAKER_02:**
[4462.3s] Yeah .
[4462.3s] And as you said, like, you know, like, it's broken mode of, like, side chain surviving .
[4462.3s] Right ?
[4462.3s] Like, it real like, you know, these it it's possible .
[4462.3s] You know?
[4473.0s] I I had oh, sorry .
[4473.0s] Go ahead, Karen .
[4473.0s] I I wanted to talk quickly about,

**SPEAKER_00:**
[4478.3s] you know, this the definition of success for blockchains,
[4482.9s] market caps,
[4485.3s] and all that sort of thing .
[4485.3s] And I was looking today because so
[4489.3s] Ethereum's market cap is in the 200 billions.
[4494.6s] Ethereum Classic is still at number 28, which is quite impressive and is, you know, 2,600,000,000.0
[4500.5s] in market cap .
[4500.5s] I think market cap is probably more of an indicator of popularity
[4506.0s] than anything,
[4507.5s] rather sort of truly long term .
[4507.5s] You know, it's not quite like with companies
[4512.9s] where market cap is probably a better indicator of how important they are, but it is also still.
[4520.1s] And then if you look Yeah.
[4522.5s] So it's very liquid.

**SPEAKER_01:**
[4523.8s] If you look in CoinGecko,
[4525.8s] so Ethereum Classic is higher than Cosmos,
[4529.3s] than Filecoin,
[4530.9s] than Hedera,
[4532.4s] than Internet Computer,
[4535.0s] than than ATTOS, than Lido,
[4538.2s] than Near,
[4539.8s] than Optimism, than Arbitrum, than The Graph.
[4543.1s] You know?

**SPEAKER_00:**
[4545.4s] And so I I wanted to to follow, you know, is market cap a good goal?
[4551.0s] What what is your goal for ETC
[4554.5s] If you were trying to,
[4556.7s] you know, make up the gap with Ethereum, what you know, would you do anything differently?

**SPEAKER_01:**
[4562.3s] I mean, I think to to do that, you you just need vast
[4566.5s] investment into
[4568.0s] application layer.
[4570.8s] I mean, I think I think that's somewhere where ETC really
[4574.8s] can't compete with many other VC chains,
[4578.8s] you know, that have huge treasuries that can be spending, you know, tens or hundreds of millions on on grant programs .
[4578.8s] You know ?
[4578.8s] That's
[4586.9s] you know, we we can't compete that way .
[4586.9s] But, also,
[4590.3s] it
[4591.2s] as you say, it it it's a bit of a vanity metric in a way .
[4591.2s] You know ?
[4591.2s] Like, there are many other vanity metrics that we we come in to see in the space
[4602.4s] because, yeah, you know, if you want whatever the fastest chain or the most
[4606.9s] money or whatever, like, yeah, that's not gonna be ETC .
[4606.9s] Like, it can never be ETC.
[4613.7s] But for people that are interested, that's not the goal .
[4613.7s] Right ?
[4613.7s] They,
[4618.1s] you know, they're they're they're they're looking for something which is basically like Bitcoin plus smart contracts, you know, with that kind of
[4625.8s] strong
[4626.6s] nonintervention
[4628.6s] kind of bias.
[4630.2s] And also proof of work, you know, a lot of people see,
[4633.6s] you know, real value in proof of work and are very skeptical of
[4638.6s] of proof of stake systems .
[4638.6s] So,
[4641.8s] you know,
[4645.3s] it's not, you know, it's not a winner takes all.

**SPEAKER_00:**
[4649.0s] It's it's been interesting just how not a winner takes all the blockchain space has been .
[4649.0s] They've they've had this they're like cockroaches.
[4656.4s] They just kinda
[4658.5s] they, you know, keep going .
[4658.5s] I know they get delisted occasionally,
[4662.3s] but, you know, how many let's see how many pages you can get to on Yo .
[4662.3s] Can we call them tree clippings

**SPEAKER_02:**
[4667.4s] instead of Yeah.

**SPEAKER_01:**
[4669.6s] 20,000
[4670.5s] is the the big.
[4672.7s] Yeah .
[4672.7s] 20,000 live chains.

**SPEAKER_02:**
[4675.0s] Yeah.

**SPEAKER_00:**
[4676.0s] That's that's quite a number and and very interesting
[4680.1s] kind of in and of itself .
[4680.1s] Victor, you you were saying something when I made my comment .
[4680.1s] Oh, no .
[4680.1s] No .
[4680.1s] No .
[4680.1s] I was just saying, I

**SPEAKER_02:**
[4686.9s] was gonna ask you more questions about,
[4691.1s] you know, the early days of EEA, but I think we will have to invite you back because I'm pretty sure we could have another,
[4700.2s] you know, another ninety minute conversation on that .
[4700.2s] But it's been great to have you, Bob .
[4700.2s] As always, you're always been a great friend and a wealth of information on the space .
[4700.2s] So thank you for joining us, and we hope you'll come back again soon.

**SPEAKER_01:**
[4715.0s] Well, thank you, and
[4716.7s] sorry for monopolizing

**SPEAKER_00:**
[4718.4s] me .
[4718.4s] No .
[4718.4s] This is exactly what it is .
[4718.4s] Why you're here .
[4718.4s] Yeah .
[4718.4s] We Exactly .
[4718.4s] Your story, we've told plenty of ours .
[4718.4s] Should we
[4726.4s] you know, I see on on other podcasts, Should we send people anywhere?
[4731.3s] Where can people find you ?
[4731.3s] Do you want them to find you, etcetera?

**SPEAKER_01:**
[4735.5s] Yeah .
[4735.5s] I can, yeah, I can I can I can drop you some links afterwards?
[4739.3s] But, yeah, my own website is bobsandworld.com.
[4743.2s] Ethereumclassic.org
[4744.8s] is is the main sort of landing page for
[4748.2s] for ETC.

**SPEAKER_00:**
[4750.4s] Awesome .
[4750.4s] Fantastic .
[4750.4s] Well, thank you very much .
[4750.4s] Really appreciate your time .
[4750.4s] And Yeah .
[4750.4s] I'm sure we will follow-up .
[4750.4s] We'll put our heads together and

**SPEAKER_02:**
[4758.8s] do another one when we're ready .
[4758.8s] We'll have to have a round two .
[4758.8s] There's plenty there's plenty more stories that we haven't even touched on yet.

**SPEAKER_01:**
[4767.3s] Okay .
[4767.3s] Care .
[4767.3s] Cheers, guys .
[4767.3s] Alright .
[4767.3s] Cheers.
