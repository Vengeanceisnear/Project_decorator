# def check_code(original_function, secret_code):
#     def wrapper():
#         user_input = input("Введите секретный код: ")
#         if user_input == secret_code:
#             original_function()
#         else:
#             print("Неверный код. Доступ запрещен.")
#     return wrapper

# def my_secure_function():
#     print("Доступ разрешен. Выполняется важная операция.")

# secured_function = check_code(my_secure_function, "секрет123")
# secured_function()
     
 
def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Вызов функции. Количество вызовов: {wrapper.calls}")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper

@counter
def example_function():
    print("Функция выполняется")

# Пример использования
example_function()
example_function()
example_function()