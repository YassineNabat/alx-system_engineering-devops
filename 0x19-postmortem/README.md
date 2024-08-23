<h1>Issue Summary</h1>
On August 20, 2024, from 09:00 to 12:30 UTC, our internal HR application experienced an outage, affecting 75% of employees trying to access the platform. During this time, users were unable to log in, submit leave requests, or view employee records. The root cause was a miscommunication between the authentication service and the database due to a broken API endpoint, which resulted in failed login attempts and data retrieval errors.

<h2>timeline</h2>
09:00 UTC - The issue was detected after multiple complaints from employees unable to log into the HR system.
09:10 UTC - Initial investigation began, assuming a network-related problem due to a high number of failed authentication requests.
09:30 UTC - Web server logs reviewed; no network-related issues found. Attention shifted to the authentication service.
09:50 UTC - Authentication service logs revealed repeated API failures when querying the employee database for user credentials.
10:15 UTC - The issue was escalated to the database and backend teams to investigate the API and database connection.
10:45 UTC - It was discovered that a recent update to the database schema had broken the authentication service’s API endpoint.
11:30 UTC - The API endpoint was reconfigured, and login functionality was tested across multiple environments.
12:00 UTC - The application was fully functional for all users, and system stability was confirmed.
12:30 UTC - Incident resolved, with services restored and normal operations resumed.
Root Cause and Resolution
Root Cause: The issue was caused by a recent schema change in the employee database that inadvertently broke an API endpoint used by the authentication service. The updated schema required an adjustment to the API’s query structure, which was not made during the update, causing authentication failures for most users.

Resolution: Once the broken API endpoint was identified, the database team quickly modified the schema to ensure compatibility with the authentication service. The backend team updated the API queries accordingly, and after successful testing, the HR application resumed normal operations.

<h1>Corrective and Preventative Measures</h1>
To prevent similar incidents in the future, the following steps will be taken:

<h2>Improvements:</h2>

Pre-Deployment Testing: Implement more rigorous pre-deployment testing, particularly for critical services like authentication, to ensure schema changes do not break existing functionality.
Continuous Integration (CI) Pipelines: Enhance the CI pipeline to include automatic testing of API endpoints whenever schema changes are made.
Versioning of APIs: Introduce version control for APIs to avoid breaking changes when updates are made to the database.
<h2>Specific Tasks:</h2>

Update API Documentation: Review and update API documentation to reflect the latest schema changes.
Add Automated Tests for API Endpoints: Create automated tests that verify the functionality of API endpoints after each deployment.
Establish API-Database Compatibility Checks: Set up regular checks to ensure API queries are compatible with the current database schema.
Conduct Post-Update Monitoring: Implement immediate post-update monitoring to detect and resolve potential issues early.
