#Concerts Database Manager

This program manages a simple SQLite database for tracking concerts, bands, and venues. It includes functionality for creating tables, inserting sample data, and retrieving information related to bands, venues, and concerts.

#Overview

The database consists of three main tables:
Bands: Stores information about musical bands (name, hometown).
Venues: Stores information about concert venues (title, city).
Concerts: Records concerts with references to bands and venues, as well as the date of the concert.
#Features

-Database Creation

Creating Tables: The create_tables() function sets up the database by creating tables for bands, venues, and concerts if they don't already exist.
-Inserting Data
Sample Data: The insert_sample_data() function adds sample bands, venues, and concerts to the database.

-Band Methods

Retrieve details about the band performing at a specific concert.
Find all concerts played by a specific band.
List the venues where a band has performed.
Add a new concert for a band at a specific venue and date.
Generate a band’s introduction for each city they perform in.
Find the band that has performed the most concerts.

-Venue Methods

Retrieve details about the venue where a concert is held.
Find all concerts scheduled at a specific venue.
List all bands that have performed at a venue.
Check if a concert is scheduled at a venue on a specific date.
Find the band that has performed the most at a particular venue.

-Concert Methods

Check if a concert is a hometown show for the band.
Generate a concert introduction for the band performing at a specific venue.
How to Use
Set up the database by running the create_tables() function.
Insert sample data using the insert_sample_data() function.
You can then use the various methods to retrieve information about concerts, bands, and venues, or to add new data to the database.
Dependencies
SQLite3 is used for database management.









