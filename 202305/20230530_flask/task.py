from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def user(name):
    for _ in range(5):
        return name * 5



# def find_leap_years(start_year, end_year):
#     leap_years = []
#     for year in range(start_year, end_year + 1):
#         if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#             leap_years.append(year)
#     return leap_years

# @app.route('/leap')
# def leap_years():
#     start_year = 1900
#     end_year = 2100
#     leap_years = find_leap_years(start_year, end_year)
#     return render_template('leap.html', leap_years=leap_years)

if __name__ == '__main__':
    app.run(debug=True)