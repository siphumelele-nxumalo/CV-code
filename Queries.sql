--Database and tables were created beforehand

use CV_code;

Basic queries 
---------------------------------------------

Returns a list of all employee last names and their salary in alphabetical order of surnames.

select l_name, 'R' + convert(varchar, salary) as 'Salaries' 
from Employee 
order by l_name asc;

--Generation of a unique password for Employees to access the office. Each password is dervied by taking the last 3 letters of their surname, the first 3 
--letters of their first name, followed by a dash and their epmloyee id multiplied by 4. Selects their first name, last name and password for each employee.
--This can be coupled with a python script to import a hashing algorithm such as SHA-256 to create the passwords.

select f_name, l_name, right(l_name,3) + left(f_name,3) +'-' + Convert(varchar,employee_id*4) as 'Unique Password' 
from Employee;

--Generates an overview of the highest salary, lowest salary, the total number of salaries for all the employees and the net amount for payroll. 

select 'R'+ convert(varchar,max(salary)) as 'Highest Salary', 'R'+ convert(varchar,min(salary)) as 'Lowest Salary', 
count(salary) as 'Number of Salaries', 'R'+ convert(varchar,sum(salary)) as 'Net Amount for Payroll' 
from Employee;


 Intermediate queries
 ---------------------------------------------------------
 
 --Demonstartion of the charindex() function to round up people who work in a specific department and meet a certain criteria.
 
 select f_name, l_name, charindex('a',f_name) as 'Letter Position' 
 from Employee 
 where department = 'Finance' and right(l_name,1) = 'a' ;

 --Displaying the postion names in descending order of appearences.

 select position_name 
 from Position 
 group by position_name 
 order by count(*) desc;

--Displaying which columns in the Position table have repeating values and how many times they are repeated.

 select position_name, starting_date, count(*) as 'Number of Times Repeated' 
 from Position 
 group by position_name, starting_date having count(*) > 1 ;

--Displays the first name, surname and position name of any employee who has 'Manager' in their title

select f_name, position_name
	from Employee a
	join Position c on a.employee_id = c.reference_id 
		where c.position_name like '%Manager%';

Advanced queries
---------------------------------------------------------
  
--Finds the number of employees in each department that meet a certain criteria in descending order.

select department, count(employee_id) as 'Number of Employees' 
from Employee 
where employee_id % 2 <> 0 
group by department 
order by [Number of Employees] desc;

--Calculates which Employees are due for a promotion based on the amount of months they have worked. Any employee who has worked for more than 7 years and 8 months should be promoted. Those who have worked less need more experience. Ordering the output by their level of experience.

 select f_name, l_name,
	case
		when datediff(month, hired_date, GETDATE()) > 94
		then 'Should be Promoted'
		else 'Needs more Experience'
	end as 'Promotion Decision'
	from Employee
	order by hired_date;

--Obtains the details of Employees who joined the company in Febuary 2014 and displays a column called 'Gross Income' depicting their gross income rounded off to 2 decimal places after taxes.
--Note: Gross income is base income plus commission amount. Base income is taxed at 15% and commission based income is taxed at 25%. The original data was not altered to do thisto do this.

  select * , 'R'+ convert(varchar, convert(decimal(9,2), (salary - salary * 15/100 + commission_amount - commission_amount * 25/100))) as 'Gross Income'
	from Employee a
	 join Commission b on a.employee_id = b.reference_id\
   where year(hired_date) = 2014 and month(hired_date) = 2;
 
 --Creates a view called 'commission earners' that shows the employee id, first name, last name, hired date, department and position name for all employees who earn a commission.
 
create view commission_earners as 
select distinct employee_id, f_name, l_name, hired_date, department, position_name
from Employee a
	join Commission b on a.employee_id = b.reference_id 
	join Position c on c.reference_id = b.reference_id
  where b.reference_id is not null;

select * from commission_earners;

--Creates a procedure called 'experience diff' that shows the difference in experience in days, months and years between employees who earn commission.
 
 create procedure experience_diff as
 select c.f_name, a.f_name,
		datediff(day,c.hired_date,a.hired_date) as 'Age diff in days',
		datediff(month,c.hired_date,a.hired_date) as 'Age diff in months',
		datediff(year,c.hired_date,a.hired_date) as 'Age diff in years'
		from
			commission_earners c
			join commission_earners a on c.f_name < a.f_name;

exec experience_diff;

	
	
