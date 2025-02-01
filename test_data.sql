INSERT INTO roles (id, name, permissions) VALUES
(0, 'superuser', '["all"]'),
(1, 'admin', '["create", "delete"]'),
(10, 'user', '["profile"]');

INSERT INTO profiles (role_id, name, family_name, fathers_name, birthday, phone_number, tg_username, is_deleted) VALUES
(10, 'Дмитрий', 'Акимов', 'Валерьевич', '1988-01-02', '+79165686393', 'dim-akim', False),
(10, 'Данила', 'Бланк', 'Алексеевич', '1987-07-03', '+79153333333', 'danilablank', False),
(10, 'Тимофей', 'Стародубцев', 'Михайлович', '2016-05-12', '+79222332323', 'timostar', False)
