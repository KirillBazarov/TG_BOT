from jinja2 import Template

go_text = "Бот покажет куда ты можешь задонить.Вот пару направлений"


tm_for_napravlenie = Template('так ты выбрал направление {{napravlenie}}, теперь выбирем сам фонд')