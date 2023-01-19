import statistics

from bs4 import BeautifulSoup
import psycopg2
import random

html = """<html>
<head>
<title>Our Python Class exam</title>

<style type="text/css">
	
	body{
		width:1000px;
		margin: auto;
	}
	table,tr,td{
		border:solid;
		padding: 5px;
	}
	table{
		border-collapse: collapse;
		width:100%;
	}
	h3{
		font-size: 25px;
		color:green;
		text-align: center;
		margin-top: 100px;
	}
	p{
		font-size: 18px;
		font-weight: bold;
	}
</style>

</head>
<body>
<h3>TABLE SHOWING COLOURS OF DRESS BY WORKERS AT BINCOM ICT FOR THE WEEK</h3>
<table>
	
	<thead>
		<th>DAY</th><th>COLOURS</th>
	</thead>
	<tbody>
	<tr>
		<td>MONDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, BLUE, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>TUESDAY</td>
		<td>ARSH, BROWN, GREEN, BROWN, BLUE, BLUE, BLEW, PINK, PINK, ORANGE, ORANGE, RED, WHITE, BLUE, WHITE, WHITE, BLUE, BLUE, BLUE</td>
	</tr>
	<tr>
		<td>WEDNESDAY</td>
		<td>GREEN, YELLOW, GREEN, BROWN, BLUE, PINK, RED, YELLOW, ORANGE, RED, ORANGE, RED, BLUE, BLUE, WHITE, BLUE, BLUE, WHITE, WHITE</td>
	</tr>
	<tr>
		<td>THURSDAY</td>
		<td>BLUE, BLUE, GREEN, WHITE, BLUE, BROWN, PINK, YELLOW, ORANGE, CREAM, ORANGE, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, GREEN</td>
	</tr>
	<tr>
		<td>FRIDAY</td>
		<td>GREEN, WHITE, GREEN, BROWN, BLUE, BLUE, BLACK, WHITE, ORANGE, RED, RED, RED, WHITE, BLUE, WHITE, BLUE, BLUE, BLUE, WHITE</td>
	</tr>

	</tbody>
</table>

<p>Examine the sequence below very well, you will discover that for every 1s that appear 3 times, the output will be one, otherwise the output will be 0.</p>
<p>0101101011101011011101101000111 <span style="color:orange;">Input</span></p>
<p>0000000000100000000100000000001 <span style="color:orange;">Output</span></p>
<p>
</body>
</html>"""

soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table')

colors_by_day = {}
for row in soup.select('table tr'):
    day = row.select_one('td:first-child').text
    color_string = row.select_one('td:nth-child(2)').text
    colors_of_day = color_string.split(',')
    for color in colors_of_day:
        color = color.strip()
        if color in colors_by_day:
            colors_by_day[color] += 1
        else:
            colors_by_day[color] = 1

total_colors = sum(colors_by_day.values())
# Question1 : To find the mean color
color_mean = total_colors / len(colors_by_day)
print("The mean color is:", color_mean)

# Question2 : To find the most common color
most_common_color = max(colors_by_day, key=colors_by_day.get)
print("The most common color is:", most_common_color)

# Question3 : To find the median color
color_median = statistics.median(colors_by_day.values())
print(color_median)

# Question4 : To find the variance of the color
color_variance = statistics.variance(colors_by_day.values())
print("The color variance is:", color_variance)

# Question5 : To find the probability of RED
red_count = colors_by_day.get("RED", 0)
red_probability = red_count / total_colors
print("The probability of red is:", red_probability)
#
# # Question 6 : To add color and frequency to postgresql database
connection = psycopg2.connect(
    host="My_host_name",
    database="postgresql",
    user="my_username",
    password="my_password"
)

cursor = connection.cursor()

# create table to store colors and frequencies
cursor.execute('''
    CREATE TABLE colors(
        color VARCHAR(255) NOT NULL,
        frequency INT NOT NULL
    )
''')

# insert colors and frequencies into table
for color, frequency in colors_by_day.items():
    cursor.execute(f"INSERT INTO colors (color, frequency) VALUES ('{color}', {frequency})")

connection.commit()


# Question 7 : Recursive searching algorithm
def recursive_search(numbers, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if numbers[mid] == target:
        return mid
    elif numbers[mid] > target:
        return recursive_search(numbers, target, start, mid - 1)
    else:
        return recursive_search(numbers, target, mid + 1, end)


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = int(input("Enter a number to search for: "))
result = recursive_search(numbers, target, 0, len(numbers) - 1)
if result == -1:
    print("Number not found.")
else:
    print(f"Number {target} found at index {result}.")


# Question 8 : Random 4 digits of 0s and 1s
binary_num = ''.join([str(random.randint(0, 1)) for _ in range(4)])

# convert the binary number to base 10
base10_num = int(binary_num, 2)
print(f"Generated binary number: {binary_num}")
print(f"Converted base 10 number: {base10_num}")

# Question 9 : A program to sum first 50 fibbonacci sequence
number = 50

n1 = 0
n2 = 1
sum = 0

for num in range(0, number):
    sum = sum + n1
    next = n1 + n2
    n1 = n2
    n2 = next

print("\nSum of Fibonacci Series Numbers: %d" %sum)