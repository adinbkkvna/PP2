--task 1
CREATE OR REPLACE FUNCTION get_contacts_by_pattern(p TEXT)
RETURNS TABLE(name TEXT, phone VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT
        c.first_name || ' ' || c.last_name,
        c.phone
    FROM contacts c
    WHERE c.first_name ILIKE '%' || p || '%'
       OR c.last_name ILIKE '%' || p || '%'
       OR c.phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

--task 4
CREATE OR REPLACE FUNCTION get_contacts_page(
    p_limit INTEGER,
    p_offset INTEGER
    )
RETURNS TABLE (
    id INTEGER,
    first_name VARCHAR,
    last_name VARCHAR,
    phone VARCHAR,
    city VARCHAR
)
AS $$
BEGIN
    IF p_limit < 0 OR p_offset < 0 THEN
        RAISE EXCEPTION 'Limit and offset cannot be negative';
    END IF;
    RETURN QUERY
    SELECT
        c.id,
        c.first_name,
        c.last_name,
        c.phone,
        c.city
    FROM contacts c
    ORDER BY c.id
    LIMIT p_limit
    OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;