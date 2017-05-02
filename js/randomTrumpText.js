text_list = [
              "I can just see Kim Jong saying this as Trump offers him some laced meth with Pence at his side",
              "And then we got super owned by soviet union for another 50 years and yet there are people who still vote communists too. I mean, US has people who voted for Trump for gods sake. There are dumb people everywhere.",
              "> And then we got super owned by soviet union for another 50 years and yet there are people who still vote communists too. I mean, US has people who voted for Trump for gods sake. There are dumb people everywhere.   Yeah good point. ",
              "The reason these people support facism is because they're scared of Eastern Europe becoming more diverse. That's all it is, they're driven by tribal racism, not any historical knowledge or logic. They're like the Trump supporters, they just want to remove non-whites from their countries, they want to build walls and deport people who have dark skin. They are scum and deserve non-stop social ridicule, its sickening that their mentality is making a come back in the West as anti-refugee and anti-immigrant parties rise. Even worse the Russian troll factory is promoting their hateful ideas all over Reddit and other social media platforms. This is why its so important to shame Trump supporters for voting for him, people respond to social pressure more than reason and logic. The reality is that people will abandon their knee jerk racist views if it's socially damaging, that's largely how we defeated so much racism in the past. It wasn't logic and in-depth arguements that stopped the KKK, it was it becoming socially shameful to join the klan. edit: Just got a racist PM from a Trumpet. Stay classy.",
              "That is bullshit. I am not a trump supporter, but they do not hate non white people. Go look how much upvotes a black trump supporter post gets. Gee whiz",
              "Dehumanization happens more often than you think. Like you're suggesting, yup Trump does it too. He makes these outrageous statements, and then even when people demand he repent (and he does) the fact remains he DID say that to his followers, and the backpedal often falls onto deaf ears. To some, he \"said what had to be said\" and he only repented because he was FORCED to by his \"enemies\". Which obviously isn't true. From every war, WWI, WWII, Korea, Vietnam, etc etc imagry like The Huns (germans) and Japs, to words like \"gooks\" or for US troops in the middle east \"Towel-heads and sand n*ers\" were used as well. A while back, the armed forces actually started a campaign AGAINST officers and the like using these words to attempt dehumanization.  It's really neat they're doing so, as while dehumanization makes it easier to kill someone you don't believe is equal to you, it's not healthy nor should it be used by the US Armed Forces.",
              "> Honestly that's the route to effective change, alienating and to an extent marginalizing people just leads to further radicalization(see: middle-east). Also, see US politics or reddit.  Trump supporters and many conservatives look at liberals as what's wrong with America and that liberalism is a mental disorder.  Liberals look at Trump supporters and conservatives as racist, bigots, misogynists that want nothing but white male superiority.  You can see the exact same insults and name calling in T_D as you do in r/Liberal or r/esist.",
              "That's a bit too far, I'm guessing you're from the US. You can't really make jokes at any country when your president is Donald trump.  Reply when you finish shooting up a school.",
              "Ok.  All done. Don't blame me for Trump.  I voted for Donald Duck.",
              "Yeah that's basically how Trump got millions of free air time and press during his campaign.",
              "I voted for trump because I believed the market would adjust for renewables and it force the private sector/public sector to make these obviously good decisions. Basically I'm going to saw my leg off until you start respecting the environment.",
              "i prefer this to the feds telling everyone what to do. it doesn't matter if trump agrees, or if the epa is making their rules or not. if corporations or cities or states want to be sustainable, go for it. however, what is the real plan? what are the consequences for not reaching this plan? where is the money coming from? what about all the bats and birdies that wind turbines kill? we'll see how it works out in 20 years...",
              "I saw Atlanta and thought sweet Donald Glovers second season is coming out soon",
              "Found the Trump supporter. ",
              "\"This just in: Trump administration designates coal as a \"clean energy source\" for legal purposes\". ",
              "So you don't support Trump but reguarly jerk yourself off on t_d? Right..... Why don't you read up on LCOE, and basic economics. On-shore wind is pretty much the cheapest power source there is. It is virtually identical to natural gas in terms of cost. I havent read a ton on Georgetown but I am guessing you are whining about initial principle costs for building wind turbines, and ignoring actual accounting - meaning the money that will be saved over the total life of said wind turbine. I am assuming they are building on-shore wind because they are somewhere in Texas, and wind generation works quite well there. ",
              "It could power the Trump administration\u2026 Sorry, never mind. I'm thinking TOO big.",
             ];

name_list = [
              "fuckyou2258",
              "venomae",
              "_rknews",
              "skybox9",
              "pandabear201",
              "Sam-Gunn",
              "RoleModelFailure",
              "AlphaWolf901",
              "TokeyWakenbaker",
              "rycia007",
              "FormlessAllness",
              "caine269",
              "EatGarbageDip",
              "TheFilthiestCuck",
              "Woodrow_Butnopaddle",
              "TheFilthiestCuck",
              "bonelessevil",
             ];

rank_list = [
              3,
              9,
              14,
              5,
              1,
             ];

var amount = text_list.length;
$("#numberofComments").text(amount);

$("#comment1").text(text_list[rank_list[0]]);
$("#comment2").text(text_list[rank_list[1]]);
$("#comment3").text(text_list[rank_list[2]]);
$("#comment4").text(text_list[rank_list[3]]);
$("#comment5").text(text_list[rank_list[4]]);

$("#author1").text("- /u/" + name_list[rank_list[0]]);
$("#author2").text("- /u/" + name_list[rank_list[1]]);
$("#author3").text("- /u/" + name_list[rank_list[2]]);
$("#author4").text("- /u/" + name_list[rank_list[3]]);
$("#author5").text("- /u/" + name_list[rank_list[4]]);

var counter = 0

function replaceText(){
  text = text_list[counter];
  if(text.length > 80){
    trump_array = ["Trump","trump","Donald","donald"];
    for(var i=0; i < trump_array.length; i++){
      index = text.indexOf(trump_array[i]);
      if(index > -1){
        if(index > 200){
          text = text.substring(index - 200, index) + text.substring(index,index+206);
          text = "... " + text + " ...";
        }
        else{
          diff = 200 - index;
          text = text.substring(0, index) + text.substring(index, index+206 + diff);
          text = text + " ...";
        }
      }
    }
  }
  $("#comment").text(text + " -/u/" + name_list[counter]);
  counter += 1;
  if((counter % amount) == 0){
    counter = 0;
  }
}

function reload(){
  location.reload();
}

replaceText();
setInterval(replaceText,10000);
setInterval(replaceText,600000);