name = 'Серебрянная ложка'
description = (
	'Её не существует. Не сгибать!'
)

price = 3

usable = True
def on_use(user, reply):
	reply('Ты пытаешься согнуть ложку и..')
	if user.get_mana_damage() < 150:
		reply(
			'Как ты ни пытался, столовый прибор форму не изменил. Все руки в '
			'кровь стёр. Что-то ты делаешь не так, кажется, *тебе не хватает '
			'интеллекта*. Попробуй ещё разок, когда поумнеешь. '
		)
	else:
		reply(
			'Ты вылупился на ложку и потерял концентрацию, когда увидел своё '
			'лицо в отражении и засмеялся. Но во второй раз всё получилось. '
			'Ложка обвисла. В этот момент всё стало на свои места, чья-то '
			'невидимая рука бесцеремонно дёрнула тебя вверх и в глазах потемнело.'
		)
		reply('Продолжение следует!')