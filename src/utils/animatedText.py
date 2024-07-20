import random

def animatedText(text):
    colors = ["#ff4500", "#ff8c00", "#ffd700", "#adff2f", "#00fa9a", "#00bfff", "#da70d6"]
    animated_text = "".join([f'<span style="color:{random.choice(colors)};">{char}</span>' for char in text])
    return animated_text
