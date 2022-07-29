import regex as re
import emoji
from emoji import emojize

# Text from which you want to extract emojis
text = 'We 😊 want 😅 to 😏 extract 😁 these 😀 emojis 😍'
# Using regular expression to find and extract all emojis from the text
emojis = re.findall(r'[^\w\⁠s,. ]', text)
print(emojis)



print(emojize(":thumbs_up:"))

print("\N{smiling face with sunglasses}")
print("\N{kiss mark}")

# string = "Baby I love u very much baby " + "\N{kiss mark}"
string = "Baby I love u very much baby " + "\N{kiss mark}"
print(string)

text = ":-@"
print("text :"+text +";@" +":-)")