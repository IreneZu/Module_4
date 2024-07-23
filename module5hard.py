# Различие атрибутов класса и экземпляра
# Задача "История строительства"
from time import sleep
from re import search

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    #############################################################
    # Вспомогательные функции
    #############################################################

    def __contains__(self, item):
    #    print(search('[а-яА-ЯёЁ]',item))
        is_lat = (ord('a') <= ord(item[0]) <= ord('z'))
        return (not is_lat and any(item == obj.title for obj in self.videos) or
                is_lat and any(item == obj.nickname for obj in self.users))

    def get_video(self, item):
        if item in self:
            return self.videos[self.videos.index(item)]
        else:
            return None

    def get_user(self, item):
        if item in self:
            return self.users[self.users.index(item)]
        else:
            return None

    #############################################################
    #      О с н о в н ы е    ф у н к ц и и
    #############################################################

    def log_in(self, nickname, password):
        self.log_out()
        user = self.get_user(nickname)
        if user and hash(password) == user.password:
            self.current_user = user
        elif not user:
            print(f'Пользователь {nickname} не найден.')
        else:
            print('Забыли пароль? Вспоминайте...')

    def register(self, nickname, password, age):
        user = self.get_user(nickname)
        if user:
            print(f"Пользователь {nickname} уже существует")
            # self.log_out()
        else:
            self.users.append(User(nickname, hash(password), age))
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        [self.videos.append(video) for video in videos if video.title not in self]

    def get_videos(self, str_to_find):
        return([video.title for video in self.videos if str_to_find.lower() in video.title.lower()])

    # Смотрим кино !!!
    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        if title in self:
            video_obj = self.get_video(title)
            if video_obj.adult_mode and self.current_user.age < 18:
                print("Вам нет 18 лет, пожалуйста покиньте страницу")
                return

            while video_obj.time_now < video_obj.duration:
                video_obj.time_now += 1
                print(video_obj.time_now, end = ' ')
                sleep(1)
            else:
                print('Конец видео')
                video_obj.time_now = 0


#############################################################№№№№№№№№№№№
#  Другие классы
#############################################################№№№№№№№№№№№
class Video:
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title.lower() == other.lower()


class User:
    def __init__(self, name, password, age):
        self.nickname = name
        self.password = password
        self.age = age

    def __eq__(self, other):
        return self.nickname.lower() == other.lower()

    def __repr__(self):
        return self.nickname

##########################################################################
#  Код для проверки:

ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

ur.watch_video('Для чего девушкам парень программист?')

# Проверка на вход пользователя и возрастное ограничение
# РЕГИСТРАЦИЯ
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

#  Проверка логина
print()
ur.log_in('vasya_pupkin', 'kekcheburek')

