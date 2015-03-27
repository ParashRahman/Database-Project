
insert into people values( '0', 'Jian Le Tang', 170, 61, 'black', 'black', '23-69 Avenue ThugStreet, Edmonton, AB, Canada', 'm', to_date('01011995', 'DDMMYYYY') );
insert into people values( '1', 'Randy Hu', 180, 400, 'black', 'black', 'Marcos, Edmonton', 'm', to_date('01011995', 'DDMMYYYY') );
insert into people values('2', 'Mustafa Murad', 170, 70, 'black', 'black', 'University of Toronto, Toronto, Canada', 'm', to_date('01011995', 'DDMMYYYY') );
insert into people values( '3', 'Towqir', 180, 70, 'black', 'black', 'Edmonton', 'm', to_date('10071993', 'MMDDYYYY' ) );
insert into people values ( '4', 'Tian', 160, 9, 'black', 'black', 'Calgary', 'm', to_date( '03031994', 'MMDDYYYY' ) );
insert into people values ( '5', 'Juicy J', 170, 60, 'brown', 'black', 'da hud, Compton', 'm', to_date( '02291988', 'MMDDYYYY' ) );
insert into people values ( '6', 'Danial Stahl', 180, 80, 'dark brown', 'black', '123 poop street', 'm', to_date( '07161995', 'MMDDYYYY' ) );

insert into vehicle_type values( 0, 'Car' );
insert into vehicle_type values( 1, 'Truck' );
insert into vehicle_type values( 2, 'SUV' );
insert into vehicle_type values( 3, 'Van' );

insert into vehicle values( '0', 'Toyota', 'Corolla', 2012, 'white', 0 );
insert into vehicle values( '1', 'Mercury', 'Mountaineer', 2009, 'gray', 2 );
insert into vehicle values( '2', 'Dodge', 'Caravan', 2007, 'blue', 3 );
insert into vehicle values( '3', 'Cadilac', 'Escalade', 2008, 'black', 2 );
insert into vehicle values( '4', 'Ford', 'Explorer', 2005, 'gray', 2 );
insert into vehicle values( '5', 'GMC', 'Suburban', 2006, 'pink', 2 );
insert into vehicle values( '6', 'Chevrolet', 'Tahoe', 2009, 'red', 2 );

insert into drive_licence values ( '0', '1', 'nondriving', empty_blob(), to_date( '11072010', 'DDMMYYYY' ), to_date( '11072018', 'DDMMYYYY' ) );
insert into drive_licence values ( '1', '0', 'tdriver', empty_blob(), to_date( '10102010', 'DDMMYYYY' ), to_date( '10102040', 'DDMMYYYY' ) );
insert into drive_licence values ( '4', '5', 'sup', empty_blob(), to_date( '10102010', 'DDMMYYYY' ), to_date( '10102040', 'DDMMYYYY' ) );

insert into auto_sale values ( '0', '0', '1', '2', to_date('10102009','DDMMYYYY'), 100000 );
insert into auto_sale values ( '1', '0', '1', '3', to_date('10102010','DDMMYYYY'), 10000 );
insert into auto_sale values ( '2', '0', '1', '2', to_date('10102011','DDMMYYYY'), 1000 );
insert into auto_sale values ( '3', '0', '1', '1', to_date('10102012','DDMMYYYY'), 100 );
insert into auto_sale values ( '4', '0', '1', '5', to_date('10102013','DDMMYYYY'), 10 );
insert into auto_sale values ( '5', '0', '1', '6', to_date('10102014','DDMMYYYY'), 1 );
insert into auto_sale values ( '6', '0', '1', '6', to_date('10102012','DDMMYYYY'), 1 );
insert into auto_sale values ( '7', '0', '1', '6', to_date('10102012','DDMMYYYY'), 100 );
insert into auto_sale values ( '8', '0', '1', '3', to_date( '10102011', 'DDMMYYYY' ), 100000 );
insert into auto_sale values ( '9', '0', '1', '5', to_date( '10102011', 'DDMMYYYY' ), 40 );
insert into auto_sale values ( '10', '0', '1', '5', to_date( '10102011', 'DDMMYYYY' ), 40 );
insert into auto_sale values ( 11, '0', '1', '0',  to_date( '10101995', 'DDMMYYYY' ), 40 )

insert into ticket_type values( 'speeding 1', 100 );
insert into ticket_type values( 'speeding 2', 200 );
insert into ticket_type values( 'speeding 3', 300 );
insert into ticket_type values( 'evil', 900 );

insert into ticket values ( 0, '0', '5', '2', 'evil', to_date( '10102014', 'DDMMYYYY' ), 'yo mommas house', 'ugh' );
insert into ticket values ( 1, '1', '5', '2', 'speeding 2', to_date( '10102014', 'DDMMYYYY' ), 'Las Vegas', 'Chilling like a villian' );
insert into ticket values ( 3, '3', '0', '2', 'speeding 3', to_date( '10102014', 'DDMMYYYY' ), 'suburbs', 'ran over a kid' );
insert into ticket values ( 4, '4', '0', '2', 'speeding 1', to_date( '10102014', 'DDMMYYYY' ), 'sup', 'suma' );
insert into ticket values ( 5, '4', '0', '2', 'speeding 1', to_date( '10102014', 'DDMMYYYY' ), 'sup', 'suma' );
insert into ticket values ( 6, '4', '0', '2', 'speeding 1', to_date( '10102014', 'DDMMYYYY' ), 'sup', 'suma' );
insert into ticket values ( 7, '4', '0', '2', 'speeding 1', to_date( '10102014', 'DDMMYYYY' ), 'sup', 'suma' );
insert into ticket values ( 8, '5', '0', '2', 'speeding 1', to_date( '10102014', 'DDMMYYYY' ), 'sup', 'suma' );
insert into ticket values ( 9, '5', '0', '2', 'speeding 1', to_date( '10102014', 'DDMMYYYY' ), 'sup', 'suma' );
insert into ticket values ( 10, '5', '0', '2', 'speeding 1', to_date( '10102014', 'DDMMYYYY' ), 'sup', 'suma' );

