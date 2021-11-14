from bot import const
from bot.keyboards import InlineKeyboard


class Reply:
    # (text, attachments, keyboard)
    ON_INVITE_ME = (
        "Привет! Спасибо что пригласили!\n"
        "Меня зовут @witless(Witless). Я обучаюсь на вашей переписке и затем сама пишу свои сообщения.\n"
        "\n"
        "Не забудьте выдать мне доступ ко всей переписке в настройках беседы, а то ничего не получится!\n"
        "\n"
        "Инструкция по настройке беседы для бота: https://vk.cc/9ZPoHM\n"
        "Список команд: https://vk.cc/9ZdHLN",
        None,
        InlineKeyboard.ON_INVITE_ME,
    )

    ON_HELP = (
        "Список моих команд:\n"
        "<<@witless help>> - получить список команд\n"
        "<<@witless speak {длина}>> - сгенерировать сообщение\n"
        "<<@witless bugurt>> - сгенерировать бугурт\n"
        "<<@witless dialogue>> - сгенерировать диалог\n"
        "<<@witless info>> - узнать объем сохраненных данных для обучения\n"
        "<<@witless wipe>> - сбросить данные для обучения\n"
        "<<@witless stats>> - статистика бота\n"
        "\n"
        f"Подробнее обо всех командах написано здесь: {const.Links.COMMANDS}",
        None,
        None,
    )

    HOWTO = (
        f"Инструкция по настройке беседы для бота: {const.Links.INSTRUCTION}",
        None,
        None,
    )

    ON_MENTION_ME = (
        "Вы меня звали?\n"
        "Инструкция по настройке беседы для бота: https://vk.cc/9ZPoHM\n"
        "Список моих команд: https://vk.cc/9ZdHLN",
        None,
        InlineKeyboard.ON_MENTION,
    )

    ON_GENERATING_FAIL = (
        "Я пыталась сгенерировать сообщение, но у меня ничего не получилось. "
        "Это связано с тем, что у меня еще недостаточно данных для обучения или вам просто не повезло 🤷‍♀️\n"
        "На всякий случай проверьте, выдали ли вы мне доступ ко всей переписке и продолжайте "
        "общаться",
        None,
        InlineKeyboard.ON_GENERATING_FAIL,
    )

    ON_UNKNOWN_COMMAND = (
        "Я не знаю такой команды. Список команд можно узнать тут: https://vk.cc/9ZdHLN",
        None,
        InlineKeyboard.ON_UNKNOWN_COMMAND,
    )

    ON_SPEAK_UNKNOWN_ARG = (
        "Вы указали неверный аргумент. Возможные аргументы для этой команды: "
        "<<small>>, <<medium>> и <<large>>.\n"
        f"Подробнее об этом можно узнать тут: {const.Links.COMMANDS}\n\n"
        "Вы можете использовать инлайн-кнопки, чтобы выбрать длину сообщения, которое должен сгенерировать бот",
        None,
        InlineKeyboard.ON_UNKNOWN_SPEAK_ARG,
    )

    ON_SPAM = (
        "Вы слишком часто используете эту команду. Подождите немного и попробуйте снова"
    )
