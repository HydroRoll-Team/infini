from infini.matcher import matcher, MatcherEvent


def test():
    event = MatcherEvent("rule.example_handler", string="测试")
    try:
        result = matcher.run(event)
        assert result == "捕获到输入: 测试"
    except Exception as error:
        return error
    return []

