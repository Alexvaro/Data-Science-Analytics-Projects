--1)	For each Toronto branch count the number of properties managed by their staff. Sequence the output by highest to lowest count.
SELECT COUNT(Property.PropNo) AS "Number of Properties Per Branch" FROM Property INNER JOIN Staff
ON PROPERTY.StaffNo = Staff.StaffNo INNER JOIN Branch
ON Staff.BrNo = Branch.BrNo
WHERE Branch.City = 'Toronto'
GROUP BY Branch.BrNo
ORDER BY COUNT(*) ASC

--2)	List the name and salary of the branch manager of each branch in Toronto. Sequence the output by manager name.
SELECT DISTINCT StaffName, Salary FROM Staff INNER JOIN Branch 
ON STAFF.StaffNo = Branch.MgrStaffNo
WHERE City = 'Toronto'
ORDER BY StaffName

--3)	List the name and staff # of the staff supervised by Sarah Johnson.
SELECT DISTINCT StaffName, StaffNo from Staff
WHERE SprsvrStaffNo = (SELECT SprsvrStaffNo FROM Staff WHERE StaffName = 'Sarah Johnson')

--4)	List the details for the branches where the number of employees is more than 3 and the average employee salary is 
--less than $55,000. 
SELECT DISTINCT Branch.* from Branch 
WHERE BrNo IN
(SELECT BrNo FROM Staff
GROUP BY BrNo
HAVING AVG(Salary) < 55000 AND COUNT(StaffNo) > 3)

--5)	Count the number of different property types located in Toronto that are currently leased.  
SELECT COUNT(DISTINCT PropType) FROM Property INNER JOIN LEASE
ON Property.PropNo = Lease.PropNo
WHERE City = 'Toronto' AND (EndDate > GETDATE())

--6)	List property details for detached homes (DT) in Toronto with at least 3 rooms and a monthly rent under $2,800. 
--Sequence by monthly rent - cheapest first.
SELECT DISTINCT Property.* FROM Property
WHERE PropType = 'DT' AND NoOfRooms > 2 AND MonthlyRent < 2800
ORDER BY MonthlyRent ASC

--7)	List the details of all leases for properties managed by staff in Toronto branches that will expire anytime in 2021. 
--Sequence by expiry date.
SELECT DISTINCT Lease.* FROM Lease
INNER JOIN Property
ON Lease.PropNo = Property.PropNo
INNER JOIN Staff
ON Property.StaffNo = Staff.StaffNo
INNER JOIN Branch
ON Staff.BrNo = Branch.BrNo
WHERE Branch.City = 'Toronto'
AND YEAR(Lease.EndDate) = 2021

--8)	List the details for owners with more than 2 townhouse (TH) Toronto properties. 
SELECT DISTINCT Owner.* FROM Owner
WHERE OwnerId in
(SELECT OwnerId FROM Property WHERE PropType= 'TH' AND City = 'Toronto'
GROUP BY OwnerId HAVING COUNT(*) > 2)

--9)	List the client number and name of all clients registered with a Toronto based branch.
SELECT DISTINCT Client.ClientNo, ClientName FROM Client INNER JOIN Branch
ON Client.BrNo = Branch.BrNo
WHERE Branch.City = 'Toronto'

--10)	For employees of Toronto branches list the details of the highest paid employee. 
SELECT Staff.* FROM Staff
WHERE Salary = (SELECT MAX(Salary) FROM Staff INNER JOIN Branch
ON Staff.BrNo = Branch.BrNo WHERE Branch.City = 'Toronto')

--11)	List the names of the staff who are managing any semi detached (SM) Toronto properties. Show each staff member once.
SELECT DISTINCT Staff.StaffName FROM Staff
INNER JOIN Property ON
Staff.StaffNo = Property.StaffNo
WHERE Property.PropType = 'SM' AND
Property.City = 'Toronto'

--12)	List the details for staff who manage townhouse (TH) properties that have a current lease. 
--Show each staff only once. Sequence alphabetical by name.
SELECT DISTINCT Staff.* FROM Staff INNER JOIN Property ON
Staff.StaffNo = Property.StaffNo INNER JOIN Lease ON
Property.PropNo = Lease.LeaseNo
WHERE Property.PropType = 'TH' AND
Lease.EndDate > GETDATE()

--13)	List the details for detached (DT) properties with a monthly rent higher than the average for that property type.
SELECT DISTINCT Property.* FROM Property
WHERE PropType = 'DT'
AND MonthlyRent > (SELECT AVG(MonthlyRent) FROM Property WHERE PropType = 'DT')

--14)	List in alphabetical name order the details for clients who would be interested in a detached home with a 
--monthly rent of no more than $1,750. 
SELECT DISTINCT Client.* FROM Client
WHERE TypeReq = 'DT' AND 
((PrefMaxRent < 1750) OR (PrefMaxRent = 1750))
ORDER BY Client.ClientName DESC

--15)	List the details for staff who manage more than 3 properties.
SELECT DISTINCT Staff.* FROM Staff 
WHERE StaffNo IN
(SELECT StaffNo FROM Property
GROUP BY StaffNo
HAVING COUNT(PropNo) > 3)

--16)	List the details properties that are either semi or fully detached and have a monthly rent under $1,600 a month. 
--Sequence by type within city.
SELECT DISTINCT Property.* from Property 
WHERE (PropNo = 'SM' OR PropType = 'DT')
AND MonthlyRent < 1600
ORDER BY City, PropType

--17)	List the details for properties that have current leases managed by staff working in Toronto branches.
SELECT DISTINCT Property.* FROM Property INNER JOIN Staff 
ON Property.StaffNo = Staff.StaffNo INNER JOIN Branch
ON Staff.BrNo = Branch.BrNo INNER JOIN Lease
ON Property.PropNo = Lease.PropNo
WHERE Branch.City = 'Toronto'
AND (Lease.EndDate > GETDATE())

--18)	List the details for staff who supervise more than 2 subordinates. 
SELECT DISTINCT Staff.* from Staff 
WHERE StaffNo IN
(SELECT SprsvrStaffNo FROM Staff
GROUP BY SprsvrStaffNo
HAVING COUNT(*) > 2)

--19)	List the details for owners that have both detached (DT) properties and townhouses (TH). Show each owner only once.
SELECT DISTINCT Owner.* from Owner INNER JOIN Property
ON Owner.OwnerId = Property.OwnerId
WHERE Owner.OwnerId IN
(SELECT OwnerId FROM Property
WHERE PropType = 'DT' AND PropType = 'TH')

--20)	List the details for clients registered with a Toronto branch that have leased townhouse (TH) properties, 
--either currently or in the past. Show each client only once and sequence alphabetical by name.
SELECT DISTINCT Client.* FROM Client INNER JOIN Lease
ON Client.ClientNo = Lease.ClientNo INNER JOIN Property
ON Lease.PropNo = Property.PropNo INNER JOIN Branch
ON Client.BrNo = Branch.BrNo
WHERE Branch.City = 'Toronto'
AND PropType = 'TH'
ORDER BY ClientName DESC

