-- Repairs

INSERT INTO "main"."repair" (id, name, price)
VALUES
(1, "Reparo de Freio", 15.80),
(2, "Ajuste de Marchas", 8.90),
(3, "Reparo de Pneu Furado", 5.00),
(4, "Troca de Pedal", 12.30),
(5, "Reparo de Cubo de Roda", 20.70),
(6, "Ajuste de Suspensão", 18.40),
(7, "Reparo de Guidão", 14.20),
(8, "Troca de Câmaras de Ar", 6.70),
(9, "Reparo de Quadro", 30.00),
(10, "Troca de Corrente", 10.50);

-- Clients
INSERT INTO "main"."client" (id,name,cellphone,tellphone,cep,street,number,complement,city,state)
VALUES
  (1,"Henry","(08) 9925 9262","(08) 1178 8663","717227","8603 Aenean Av.",37,"Mexico","Jambi","Dorset"),
  (2,"Keegan","(01) 3780 6968","(05) 5628 4566","2468","243-1234 Non Rd.",63,"Brazil","Tibet","Rivers"),
  (3,"Ahmed","(04) 2555 2924","(08) 6828 1527","563364","575-8233 Turpis. Ave",100,"Poland","Ivanovo","Basse-Normandie"),
  (4,"Grant","(05) 0081 8722","(08) 4894 8572","684140","943-1450 Et Street",46,"Brazil","Piedras Negras","Istanbul"),
  (5,"Norman","(07) 3416 4351","(07) 7762 7245","23-24","303 Ac Ave",75,"Norway","Raurkela Civil Township","Waals-Brabant");

-- Users
INSERT INTO "main"."auth" (id,username,user,password,email,password_hint,photo)
VALUES
  (1,"Mcbride","Colleen Olsen","GST02DUH4JX","ac@hotmail.org","Tellus Limited","metus."),
  (2,"Burns","Kirestin Owens","GHY56DPF6QJ","egestas.sed@outlook.com","Diam Pellentesque Habitant LLP","hendrerit."),
  (3,"Knowles","Diana Nicholson","IJK26SBB5TL","turpis.nec@yahoo.ca","Sed Incorporated","odio."),
  (4,"Adkins","Chava Huff","KXH07FBN1GX","quis@aol.com","Neque Sed Dictum LLC","ut,"),
  (5,"Ferguson","Dane Rogers","CKO63JYM3YS","mus.donec.dignissim@yahoo.net","Tempus Lorem Corp.","nec,");

-- Bikes
INSERT INTO "main"."bike" (id,owner,status,model,wheel,iron,color)
VALUES
  (1,5,"arcu.","ac","est,","sem,","#69dbea"),
  (2,1,"dolor","lorem","fringilla,","vel","#7961c6"),
  (3,5,"lacus.","rutrum,","luctus","Vestibulum","#59dee0"),
  (4,2,"lacinia","Nam","magnis","libero.","#6c9ddd"),
  (5,1,"metus","vehicula.","molestie","consectetuer","#2d20db");

-- Services
INSERT INTO "main"."service" (id,name,price,id_bike,id_repair)
VALUES
  (1,"ac",86,2,4),
  (2,"lorem",58,2,9),
  (3,"rutrum,",85,2,2),
  (4,"Nam",41,1,3),
  (5,"vehicula.",44,5,3);
