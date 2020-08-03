from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random_word import RandomWords
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options

# variable
dictweb = 'https://dictionary.cambridge.org/zht/'
chrome_options = Options()  # headless option
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
count = 0
b_count = 0
legin_vocab = True

# basic input
Vcount = input('How many vocab you want? ')


# vocab generating
Vgen = RandomWords()
Vlist = Vgen.get_random_words(hasDictionaryDef="true", maxLength=10, limit=Vcount)


# call for web
driver = webdriver.Chrome(executable_path='./chromedriver',options=chrome_options)
driver.get(dictweb)


def planB(nearV):   # plan for picking near word
    ActionChains(driver).click(nearV).perform()


# search
search = driver.find_element_by_id('searchword')
for vocab in Vlist:
    legin_vocab = True
    count += 1
    search = driver.find_element_by_id('searchword')
    search.send_keys(vocab)
    search.send_keys(Keys.ENTER)
    checkT = '{} - 你拼寫正確了嗎？劍橋英語-漢語（繁體）詞典中的其他拼寫方式 - 劍橋線上詞典'.format(vocab)
    if driver.title != checkT:  # check if there a word or not
        pass
    else:
        nearV = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[3]/div[1]/div[1]/ul/li[1]/a/span')
        planB(nearV)
    try:
        vocabB = driver.find_element_by_xpath('//*[@id="page-content"]/div[2]/div[4]/div/div/div/div[2]/div[1]/span/span').text
        vocab_meanC = driver.find_element_by_xpath('//*[@id="page-content"]/div[2]/div[4]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[3]/span').text
        vocabPOC = driver.find_element_by_xpath('//*[@id="page-content"]/div[2]/div[4]/div/div/div[1]/div[2]/div[2]/span').text
        vocab_mean = driver.find_element_by_xpath('//*[@id="page-content"]/div[2]/div[4]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[2]/div').text
        vocab_sample = driver.find_element_by_xpath('//*[@id="page-content"]/div[2]/div[4]/div/div/div[1]/div[3]/div/div[2]/div[1]/div[3]/div[1]/span[1]').text
    except:
        b_count += 1
        count -= 1
        legin_vocab = False
    if legin_vocab is True:
        print(count, '.) ', vocabB, '(', vocabPOC, ')', '   ', vocab_meanC)
        print('Meaning: ', vocab_mean)
        print('Example: ', vocab_sample)

print('Total:', count, ' vocab', ' + ', b_count, ' bad vocab')
print('Job done')
input('press to leave')
driver.quit()

