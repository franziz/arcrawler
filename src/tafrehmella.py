from lib.forum_engine import Template
from lib.network_tools import NetworkTools

class Crawler(Template):
	NETWORK_TOOLS = NetworkTools(use_proxy=False)
	TEMPLATE = "crawler.arct"
	TEST_TEMPLATE = "crawler_test.arct"
	DB_SERVER_ADDRESS = "mongo:27017"
	DB_SERVER_NAME = "tafrehmella"
	CRAWLER_NAME = "Tafrehmella Crawler"
	LINK_TO_CRAWL = [
		"http://www.tafrehmella.com/forums/announcement.247/",
		"http://www.tafrehmella.com/forums/introduction.251/",
		"http://www.tafrehmella.com/forums/members-guideline.698/",
		"http://www.tafrehmella.com/forums/member-reviews.763/",
		"http://www.tafrehmella.com/forums/tm-members-interview.284/",
		"http://www.tafrehmella.com/forums/coffee-with-rr.721/",
		"http://www.tafrehmella.com/forums/tm-legend.759/",
		"http://www.tafrehmella.com/forums/pakistan-super-league.791/",
		"http://www.tafrehmella.com/forums/helpdesk.713/",
		"http://www.tafrehmella.com/forums/news-fuse.753/",
		"http://www.tafrehmella.com/forums/tafreeh.266/",
		"http://www.tafrehmella.com/forums/riddles-quiz.670/",
		"http://www.tafrehmella.com/forums/teri-meri-aisi-dosti.728/",
		"http://www.tafrehmella.com/forums/tms-contest.285/",
		"http://www.tafrehmella.com/forums/eid-contests.758/",
		"http://www.tafrehmella.com/forums/best-nominations-awardz.296/",
		"http://www.tafrehmella.com/forums/baat-cheet.279/",
		"http://www.tafrehmella.com/forums/media-chat.752/",
		"http://www.tafrehmella.com/forums/become-a-columnist.327/",
		"http://www.tafrehmella.com/forums/baton-say-kushbo-aye.283/",
		"http://www.tafrehmella.com/forums/poll-question.262/",
		"http://www.tafrehmella.com/forums/tm-tube.616/",
		"http://www.tafrehmella.com/forums/greeting-congrats-and-sorrow.267/",
		"http://www.tafrehmella.com/forums/time-pass.248/",
		"http://www.tafrehmella.com/forums/mega-threads-mela.588/",
		"http://www.tafrehmella.com/forums/jokes.245/",
		"http://www.tafrehmella.com/forums/show-us-your-work.332/",
		"http://www.tafrehmella.com/forums/umm-e-ahmad.782/",
		"http://www.tafrehmella.com/forums/anadil.785/",
		"http://www.tafrehmella.com/forums/zaroon.786/",
		"http://www.tafrehmella.com/forums/seap.787/",
		"http://www.tafrehmella.com/forums/dark.788/",
		"http://www.tafrehmella.com/forums/tm-designers.674/",
		"http://www.tafrehmella.com/forums/kids-mela.640/",
		"http://www.tafrehmella.com/forums/islam-for-kids.712/",
		"http://www.tafrehmella.com/forums/kids-stories.641/",
		"http://www.tafrehmella.com/forums/kids-tube.643/",
		"http://www.tafrehmella.com/forums/kids-joke.642/",
		"http://www.tafrehmella.com/forums/kids-home-work-help.644/",
		"http://www.tafrehmella.com/forums/kids-poem.645/",
		"http://www.tafrehmella.com/forums/kids-knowledge.648/",
		"http://www.tafrehmella.com/forums/picture-gallery.650/",
		"http://www.tafrehmella.com/forums/t-m-sms.350/",
		"http://www.tafrehmella.com/forums/good-night-sms.513/",
		"http://www.tafrehmella.com/forums/new-year-sms.632/",
		"http://www.tafrehmella.com/forums/funny-sms.416/",
		"http://www.tafrehmella.com/forums/eid-mubarak-sms.417/",
		"http://www.tafrehmella.com/forums/birthday-sms.418/",
		"http://www.tafrehmella.com/forums/friendship-sms.419/",
		"http://www.tafrehmella.com/forums/love-romantic-sms.420/",
		"http://www.tafrehmella.com/forums/flirt-sms.421/",
		"http://www.tafrehmella.com/forums/islamic-sms.423/",
		"http://www.tafrehmella.com/forums/good-luck-sms.756/",
		"http://www.tafrehmella.com/forums/inspirational-quotes-sms.757/",
		"http://www.tafrehmella.com/forums/ramzan-sms.707/",
		"http://www.tafrehmella.com/forums/ascii-sms.510/",
		"http://www.tafrehmella.com/forums/good-morning-sms.512/",
		"http://www.tafrehmella.com/forums/punjabi-sms.514/",
		"http://www.tafrehmella.com/forums/islam.257/",
		"http://www.tafrehmella.com/forums/hamd-o-naat.348/",
		"http://www.tafrehmella.com/forums/islamic-question-and-answer.349/",
		"http://www.tafrehmella.com/forums/hadees-sunnah.679/",
		"http://www.tafrehmella.com/forums/quran.661/",
		"http://www.tafrehmella.com/forums/tafseer-ul-quran.685/",
		"http://www.tafrehmella.com/forums/qasas-ul-anbiya-nabio-ke-waqeeat.684/",
		"http://www.tafrehmella.com/forums/arkan-e-islam.622/",
		"http://www.tafrehmella.com/forums/eid-ul-adha-special.735/",
		"http://www.tafrehmella.com/forums/ramadan-special.705/",
		"http://www.tafrehmella.com/forums/ramadan-recipes.628/",
		"http://www.tafrehmella.com/forums/islamic-books.471/",
		"http://www.tafrehmella.com/forums/sahih-bukhari.555/",
		"http://www.tafrehmella.com/forums/pakistan-hamari-jaan.329/",
		"http://www.tafrehmella.com/forums/the-defenders.593/",
		"http://www.tafrehmella.com/forums/independence-day-pakistan.789/",
		"http://www.tafrehmella.com/forums/cricket.252/",
		"http://www.tafrehmella.com/forums/cricket-tube.767/",
		"http://www.tafrehmella.com/forums/cricket-world-cup-2015.768/",
		"http://www.tafrehmella.com/forums/sheer-o-shayari.246/",
		"http://www.tafrehmella.com/forums/yaad-shayari.734/",
		"http://www.tafrehmella.com/forums/ashaar.646/",
		"http://www.tafrehmella.com/forums/designed-poetry.378/",
		"http://www.tafrehmella.com/forums/shayari-games.415/",
		"http://www.tafrehmella.com/forums/ghazal.392/",
		"http://www.tafrehmella.com/forums/punjabi-shayri.525/",
		"http://www.tafrehmella.com/forums/romantic-shayari.393/",
		"http://www.tafrehmella.com/forums/nazam.647/",
		"http://www.tafrehmella.com/forums/sindhi-shayri.611/",
		"http://www.tafrehmella.com/forums/funny-poetry.272/",
		"http://www.tafrehmella.com/forums/ghamgheen-shayari.395/",
		"http://www.tafrehmella.com/forums/religious-shayari.396/",
		"http://www.tafrehmella.com/forums/patriotic-shayari.397/",
		"http://www.tafrehmella.com/forums/video-audio-poetry.652/",
		"http://www.tafrehmella.com/forums/tms-poet.370/",
		"http://www.tafrehmella.com/forums/ocean-of-love.783/",
		"http://www.tafrehmella.com/forums/muttalib.790/",
		"http://www.tafrehmella.com/forums/s-chiragh.668/",
		"http://www.tafrehmella.com/forums/saviou.671/",
		"http://www.tafrehmella.com/forums/famous-poet.398/",
		"http://www.tafrehmella.com/forums/abbas-tabish-poetry.699/",
		"http://www.tafrehmella.com/forums/ahmed-faraz.399/",
		"http://www.tafrehmella.com/forums/allama-iqbal.400/",
		"http://www.tafrehmella.com/forums/amjad-islam-amjad.402/",
		"http://www.tafrehmella.com/forums/faiz-ahmed-faiz.404/",
		"http://www.tafrehmella.com/forums/meer-taqi-meer.407/",
		"http://www.tafrehmella.com/forums/mir-dagh-dhelvi.411/",
		"http://www.tafrehmella.com/forums/mir-dard.405/",
		"http://www.tafrehmella.com/forums/atif-saeed.518/",
		"http://www.tafrehmella.com/forums/mirza-ghalib.406/",
		"http://www.tafrehmella.com/forums/mohsin-naqvi.440/",
		"http://www.tafrehmella.com/forums/noshi-gilani.444/",
		"http://www.tafrehmella.com/forums/perveen-shakir.408/",
		"http://www.tafrehmella.com/forums/saghir-siddiqui.442/",
		"http://www.tafrehmella.com/forums/sahir-ludhianvi.441/",
		"http://www.tafrehmella.com/forums/wasi-shah.409/",
		"http://www.tafrehmella.com/forums/javed-akhtar.481/",
		"http://www.tafrehmella.com/forums/arshad-malik.520/",
		"http://www.tafrehmella.com/forums/english-poetry.271/",
		"http://www.tafrehmella.com/forums/william-wordsworth.739/",
		"http://www.tafrehmella.com/forums/robert-frost.740/",
		"http://www.tafrehmella.com/forums/john-keats.741/",
		"http://www.tafrehmella.com/forums/emily-dickinson.742/",
		"http://www.tafrehmella.com/forums/rabindra-naath-tagore.743/",
		"http://www.tafrehmella.com/forums/rudyard-kipling.744/",
		"http://www.tafrehmella.com/forums/william-blake.489/",
		"http://www.tafrehmella.com/forums/william-shakespeare.490/",
		"http://www.tafrehmella.com/forums/james-whitcomb-riley.749/",
		"http://www.tafrehmella.com/forums/william-carlos-williams.751/",
		"http://www.tafrehmella.com/forums/urdu-novel-and-books.381/",
		"http://www.tafrehmella.com/forums/jasosi-novel.472/",
		"http://www.tafrehmella.com/forums/sachi-kahaniyan.382/",
		"http://www.tafrehmella.com/forums/mazahiya-kahanian.383/",
		"http://www.tafrehmella.com/forums/urdu-digest.710/",
		"http://www.tafrehmella.com/forums/request.534/",
		"http://www.tafrehmella.com/forums/adab-ka-daricha.660/",
		"http://www.tafrehmella.com/forums/nimra-ahmda-novels-iqtebas.764/",
		"http://www.tafrehmella.com/forums/umera-ahmed-novels-iqtebas.765/",
		"http://www.tafrehmella.com/forums/sir-ashfaque-ahmed-novels-iqtebas.766/",
		"http://www.tafrehmella.com/forums/tm-urdu-writers.633/",
		"http://www.tafrehmella.com/forums/qawareer.722/",
		"http://www.tafrehmella.com/forums/lost-passenger.723/",
		"http://www.tafrehmella.com/forums/adobe-photoshop-classes.672/",
		"http://www.tafrehmella.com/forums/education-learning.475/",
		"http://www.tafrehmella.com/forums/examination-results.669/",
		"http://www.tafrehmella.com/forums/debate-and-speech.688/",
		"http://www.tafrehmella.com/forums/question-of-the-week.691/",
		"http://www.tafrehmella.com/forums/other-languages-learning.479/",
		"http://www.tafrehmella.com/forums/lecture-videos.678/",
		"http://www.tafrehmella.com/forums/homework-help.566/",
		"http://www.tafrehmella.com/forums/free-study-notes.610/",
		"http://www.tafrehmella.com/forums/mcs-mba-notes.718/",		
		"http://www.tafrehmella.com/forums/matric-class-subject-notes.606/",		
		"http://www.tafrehmella.com/forums/2nd-year-subject-notes.608/",		
		"http://www.tafrehmella.com/forums/english-language-course.476/",
		"http://www.tafrehmella.com/forums/conversation-listening-grammer-class.478/",
		"http://www.tafrehmella.com/forums/english-vocabularies.485/",
		"http://www.tafrehmella.com/forums/recorded-english-language-course.507/",
		"http://www.tafrehmella.com/forums/craft-room.687/",
		"http://www.tafrehmella.com/forums/all-about-boys.264/",
		"http://www.tafrehmella.com/forums/fashion-and-style.335/",
		"http://www.tafrehmella.com/forums/all-about-girls.242/",
		"http://www.tafrehmella.com/forums/totkay.676/",
		"http://www.tafrehmella.com/forums/pakistani-makeup-tutorial.298/",
		"http://www.tafrehmella.com/forums/cooking.243/",
		"http://www.tafrehmella.com/forums/cooking-videos.353/",
		"http://www.tafrehmella.com/forums/mehndi-or-heena.249/",
		"http://www.tafrehmella.com/forums/home-decoration.263/",
		"http://www.tafrehmella.com/forums/health-care.250/",
		"http://www.tafrehmella.com/forums/tm-fitness.724/",
		"http://www.tafrehmella.com/forums/global-world-wide-jobs.592/",
		"http://www.tafrehmella.com/forums/current-affairs-issues.291/",
		"http://www.tafrehmella.com/forums/the-world.288/",
		"http://www.tafrehmella.com/categories/entertainment.614/", 
		"http://www.tafrehmella.com/forums/showbiz.273/",
		"http://www.tafrehmella.com/forums/celebrities-world.506/",
		"http://www.tafrehmella.com/forums/celebrities-interview.656/",
		"http://www.tafrehmella.com/forums/celebrities-images.657/",		
		"http://www.tafrehmella.com/forums/sports.716/",
		"http://www.tafrehmella.com/forums/soccer.715/",
		"http://www.tafrehmella.com/forums/tennis.447/",
		"http://www.tafrehmella.com/forums/it-news-discussion.328/",
		"http://www.tafrehmella.com/forums/mobile-mania.277/",
		"http://www.tafrehmella.com/forums/mobile-softwares.553/",
		"http://www.tafrehmella.com/forums/lataest-mobile-phone-info.565/",
		"http://www.tafrehmella.com/forums/ring-tones.373/",
		"http://www.tafrehmella.com/forums/mobile-games.376/",
		"http://www.tafrehmella.com/forums/ufone.448/",
		"http://www.tafrehmella.com/forums/jazz.449/",
		"http://www.tafrehmella.com/forums/warid.450/",
		"http://www.tafrehmella.com/forums/zong.451/",
		"http://www.tafrehmella.com/forums/telenor.452/",
		"http://www.tafrehmella.com/forums/web-related.270/"
        ]
	COUNTRY = "PHL"
	THREAD_XPATH = "//li[re:test(@id,'thread-*')]"
	THREAD_LINK_XPATH = ".//a[@class='PreviewTooltip']/@href"

	LAST_PAGE_XPATH = "(//div[@class='PageNav']//a[not(contains(text(),'Next >'))])[last()]/@href"
	PREV_XPATH = "//div[@class='PageNav']//a[contains(text(),'< Prev')]/@href"
	POST_XPATH = "//ol[@class='messageList']//li[re:test(@id,'post-*')]"
	FIELDS = [ 
		{"published_date": {
			"single": True,
			"data_type": "date",
			"concat": False,
			"xpath":"concat(.//span[@class='DateTime']/@title,.//abbr[@class='DateTime']/text())"
		}},
		{"author_name":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath": ".//a[@class='username']//text()"
		}},
		{"content":{
			"single":True,
			"data_type": "string",
			"concat":True,
			"xpath":".//div[@class='messageContent']//text()"
		}},
		{"permalink": {
			"single": True,
			"data_type": "url",
			"concat": False,
			"xpath": ".//a[@title='Permalink']/@href"
		}},
		{"title":{
			"single":True,
			"data_type": "string",
			"concat":False,
			"xpath":"//div[@class='titleBar']//h1/text()"
		}}       
	]
	CONDITIONS={
                "has_to_have_content":{
                        "condition":'"content" in document',
                        "exception":'"content is not defined"'
                },
                "has_to_have_published_date":{
                        "condition":'"published_date" in document',
                        "exception":'"published_date is not defined"'
                },
                "has_to_have_title":{
                        "condition":'"title" in document',
                        "exception":'"title is not defined"'
                },
                "has_to_have_author_name":{
                        "condition":'"author_name" in document',
                        "exception":'"author_name is not defined"'
                },
                "has_to_have_permalink":{
                        "condition":'"permalink" in document',
                        "exception":'"permalink is not defined"'
                },
                "content_cannot_be_empty":{
                        "condition":'len(document["content"]) > 0',
                        "exception":'"content cannot be empty"'
                },
                "published_date_cannot_be_empty":{
                        "condition":'document["published_date"] is not None',
                        "exception":'"published_date cannot be empty"'
                },
                "title_cannot_be_empty":{
                        "condition":'len(document["title"]) > 0',
                        "exception":'"title cannot be empty"'
                },
                "author_name_cannot_be_empty":{
                        "condition":'len(document["author_name"]) > 0',
                        "exception":'"author_name cannot be empty"'
                },
                "permalink_cannot_be_empty":{
                        "condition":'len(document["permalink"]) > 0',
                        "exception":'"permalink cannot be empty"'
                },
        }
#end class

