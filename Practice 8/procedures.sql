CREATE TABLE IF NOT EXISTS invalid_contacts (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone VARCHAR(20),
    reason TEXT
);

--task 2
CREATE OR REPLACE PROCEDURE upsert_contact(
    p_first_name VARCHAR,
    p_last_name VARCHAR,
    p_phone VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM contacts
        WHERE first_name = p_first_name
          AND last_name = p_last_name
    ) THEN

        UPDATE contacts
        SET phone = p_phone
        WHERE first_name = p_first_name
          AND last_name = p_last_name;

    ELSE

        INSERT INTO contacts(first_name, last_name, phone)
        VALUES (p_first_name, p_last_name, p_phone);

    END IF;
END;
$$;

--task 3
CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_first_names TEXT[],
    p_last_names TEXT[],
    p_phones TEXT[]
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INTEGER;
    total INTEGER;
    v_first_name TEXT;
    v_last_name TEXT;
    v_phone TEXT;
BEGIN
    IF COALESCE(array_length(p_first_names, 1), 0)
       <> COALESCE(array_length(p_last_names, 1), 0)
       OR
       COALESCE(array_length(p_first_names, 1), 0)
       <> COALESCE(array_length(p_phones, 1), 0)
    THEN
        RAISE EXCEPTION 'All arrays must have the same length';
    END IF;

    total := COALESCE(array_length(p_first_names, 1), 0);

    FOR i IN 1..total LOOP
        v_first_name := p_first_names[i];
        v_last_name := p_last_names[i];
        v_phone := p_phones[i];

        IF v_first_name IS NULL OR TRIM(v_first_name) = ''
           OR v_last_name IS NULL OR TRIM(v_last_name) = ''
           OR v_phone IS NULL
           OR v_phone !~ '^\+7[0-9]{10}$'
        THEN
            INSERT INTO invalid_contacts(
                first_name, last_name, phone, reason
            )
            VALUES (
                v_first_name,
                v_last_name,
                v_phone,
                'Invalid name or phone number'
            );

        ELSE
            INSERT INTO contacts(first_name, last_name, phone)
            VALUES (v_first_name, v_last_name, v_phone);
        END IF;
    END LOOP;
END;
$$;

--task 5
CREATE OR REPLACE PROCEDURE delete_contact(p_value TEXT)
LANGUAGE plpgsql
AS $$
DECLARE
    deleted_count INTEGER;
BEGIN
    DELETE FROM contacts
    WHERE first_name || ' ' || last_name = p_value
       OR phone = p_value;

    GET DIAGNOSTICS deleted_count = ROW_COUNT;

    IF deleted_count > 0 THEN
        RAISE NOTICE 'Contact deleted';
    ELSE
        RAISE NOTICE 'Contact not found';
    END IF;
END;
$$;
