CREATE TABLE IF NOT EXISTS kalkulacije (
    id SERIAL PRIMARY KEY,
    brend VARCHAR(100),
    proizvod VARCHAR(100),
    datum_otvaranja DATE,
    datum_isteka DATE
);