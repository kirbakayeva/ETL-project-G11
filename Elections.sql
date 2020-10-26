CREATE TABLE "Polls" (
 "state" VARCHAR,
 "pollster_id" INT,
 "pollster" VARCHAR,
 "fte_grade" VARCHAR,
 "sample_size" FLOAT,
 "population" VARCHAR,
 "methodology" VARCHAR,
 "end_date" DATE,
 "nationwide_batch" BOOL,
 "answer" VARCHAR,
 "candidate_party" VARCHAR,
 "pct" FLOAT,
 "committee_id" VARCHAR
);

ALTER TABLE "Polls"
ADD COLUMN id SERIAL PRIMARY KEY;


CREATE TABLE "Candidate_Spending" (
 "committee_id" VARCHAR,
 "disbursement_date" DATE,
 "disbursement_amount" FLOAT,
 "recipient_name" VARCHAR,
 "recipient_state" VARCHAR,
 "disbursement_description" VARCHAR 
);

ALTER TABLE  "Candidate_Spending"
ADD COLUMN id SERIAL PRIMARY KEY;

CREATE TABLE "Candidates" (
 "committee_id" VARCHAR,
 "name" VARCHAR,
 "committee_type" VARCHAR,
 CONSTRAINT "pk_Candidates" PRIMARY KEY (
  "committee_id"
  )
);

CREATE TABLE "States" (
 "State" VARCHAR UNIQUE,
 "Abbreviation" VARCHAR UNIQUE,
 "Population" INT,
 CONSTRAINT "pk_States" PRIMARY KEY (
  "State","Abbreviation"
  )
);

ALTER TABLE "Polls" ADD CONSTRAINT "fk_Polls_state" FOREIGN KEY("state")
REFERENCES "States" ("State");

ALTER TABLE "Polls" ADD CONSTRAINT "fk_Polls_committee_id" FOREIGN KEY("committee_id")
REFERENCES "Candidates" ("committee_id");

ALTER TABLE "Candidate_Spending" ADD CONSTRAINT "fk_Candidate_Spending_committee_id" FOREIGN KEY("committee_id")
REFERENCES "Candidates" ("committee_id");

ALTER TABLE "Candidate_Spending" ADD CONSTRAINT "fk_Candidate_Spending_recipient_state" FOREIGN KEY("recipient_state")
REFERENCES "States" ("Abbreviation");


SELECT * FROM "States";
SELECT * FROM "Candidate_Spending"
SELECT * FROM "Candidates"
SELECT * FROM "Polls"