# YuvaIntern Week 5 - Security Enhancements in Python Applications

## Project Overview
This project demonstrates a security review and hardening process for a Python user management application. The original application was reviewed for common security weaknesses and then improved using secure coding practices.

## Vulnerabilities Identified
1. **SQL Injection:** SQL queries were constructed using string concatenation, allowing user input to influence SQL syntax.
2. **Plain-text Password Storage:** The original application stored passwords directly.
3. **Weak Input Validation:** Usernames, emails, and passwords were not sufficiently validated.
4. **Information Leakage:** Detailed database exceptions were shown to users.

## Security Fixes
The secure version uses parameterized SQLite queries, PBKDF2-HMAC-SHA256 password hashing with a random salt, username/email/password validation, and safe database error messages.

## Testing
The secure application was tested for normal user creation and lookup. Invalid usernames, invalid emails, short passwords, and database errors were handled without exposing internal database details.

## Before and After
**Before:** String-built SQL, plain-text passwords, weak validation, and detailed errors.

**After:** Parameterized SQL, salted password hashing, input validation, and safe error handling.

## Conclusion
The project demonstrates vulnerability identification, practical security hardening, testing, and documentation for a Python application.
