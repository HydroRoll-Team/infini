from infini.matcher import matcher, MatcherEvent

def test():
    event = MatcherEvent("MyRule")
    try:
        matcher.run(event)
    except Exception as error:
        return [error]
    finally:
        return []
