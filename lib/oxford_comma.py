def oxford_comma(items):
    if len(items) == 1:
        return "".join(items)
    elif len(items) ==2:
        return " and ".join(items)
    else:
        last_item = items.pop()
        split_items = ", ".join(items)
        sentence = split_items + ", and " + last_item
        return sentence
