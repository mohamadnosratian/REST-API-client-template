"""
The MIT License (MIT)

Copyright (c) 2016 Rémy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from {{ cookiecutter.project_slug }} import __version__
import pytest

from {{ cookiecutter.project_slug }}.handlers.{{ cookiecutter.resource_name }} import Handler
{{ cookiecutter.resource_name}}_hander = Handler()

def test_version():
    assert __version__ == "{{ cookiecutter.version }}"

@pytest.mark.asyncio()
async def test_api_{{ cookiecutter.resource_name }}():
    result = await {{ cookiecutter.resource_name }}_handler.get_{{ cookiecutter.resource_name }}(data="{{ cookiecutter.project_slug }}")
    assert result == "{{ cookiecutter.project_slug }}"