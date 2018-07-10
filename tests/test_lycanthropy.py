import lycanthropy


def test_snake_to_camel():
    snake_str = 'snake_case_string'
    camel = lycanthropy.snake_to_camel(snake_str)
    assert camel == 'snakeCaseString'


def test_snake_to_pascal():
    snake_str = 'snake_case_string'
    pascal = lycanthropy.snake_to_pascal(snake_str)
    assert pascal == 'SnakeCaseString'


def test_camel_to_snake():
    camel_str = 'camelCaseString'
    snake = lycanthropy.camel_to_snake(camel_str)
    assert snake == 'camel_case_string'


def test_pascal_to_snake():
    pascal_str = 'PascalCaseString'
    snake = lycanthropy.camel_to_snake(pascal_str)
    assert snake == 'pascal_case_string'


def test_morph_dict():
    nested = {'snake_case_1': {'snake_case_2': None}}
    camel = lycanthropy.morph_dict(nested, lycanthropy.snake_to_camel)
    assert 'snakeCase2' in camel['snakeCase1']
