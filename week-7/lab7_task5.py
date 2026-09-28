from functools import wraps

is_logged_in = True

def require_login(func):
    @wraps(func)
    def wrapper():
        if is_logged_in:
            return func()
        else:
            print("Access denied. Please login first.")
    return wrapper

@require_login
def dashboard():
    print("Welcome to the dashboard!")

print("When logged in:")
is_logged_in = True
dashboard()

print("\nWhen not logged in:")
is_logged_in = False
dashboard()
#output:-
#When logged in:
#Welcome to the dashboard!

#When not logged in:
#Access denied. Please login first
