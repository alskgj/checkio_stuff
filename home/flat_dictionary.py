def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        for k, v in current.items():
            if isinstance(v, dict) and v:
                stack.append((path + (k,), v))
            elif isinstance(v, dict) and not v:
                result["/".join((path+ (k,)))] = ""
            else:
                result["/".join((path + (k,)))] = v
    return result
