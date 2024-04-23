INSERT INTO public.users (display_name, email, handle, cognito_user_id)
VALUES
  ('cruddur_yes_name', 'doronar123+cruddur_yes@gmail.com' ,'cruddur_yes_username' ,'MOCK'),
  ('Doron Arnon', 'doronar123+cruddur@gmail.com','DoronArnon' ,'MOCK');
  #Run SQL
  ('Londo Mollari','lmollari@centari.com','londo','Mock');

INSERT INTO public.activities (user_uuid, message, expires_at)
VALUES
  (
    (SELECT uuid from public.users WHERE users.handle = 'cruddur_yes_username' LIMIT 1),
    'This was imported as seed data!',
    current_timestamp + interval '10 day'
  )