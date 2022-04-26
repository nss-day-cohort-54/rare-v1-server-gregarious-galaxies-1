CREATE TABLE "Users" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "first_name" varchar,
  "last_name" varchar,
  "email" varchar,
  "bio" varchar,
  "username" varchar,
  "password" varchar,
  "profile_image_url" varchar,
  "created_on" date,
  "active" bit
);

CREATE TABLE "DemotionQueue" (
  "action" varchar,
  "admin_id" INTEGER,
  "approver_one_id" INTEGER,
  FOREIGN KEY(`admin_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`approver_one_id`) REFERENCES `Users`(`id`),
  PRIMARY KEY (action, admin_id, approver_one_id)
);


CREATE TABLE "Subscriptions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "follower_id" INTEGER,
  "author_id" INTEGER,
  "created_on" date,
  FOREIGN KEY(`follower_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Posts" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "category_id" INTEGER,
  "title" varchar,
  "publication_date" date,
  "image_url" varchar,
  "content" varchar,
  "approved" bit
);

CREATE TABLE "Comments" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "author_id" INTEGER,
  "content" varchar,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`author_id`) REFERENCES `Users`(`id`)
);

CREATE TABLE "Reactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar,
  "image_url" varchar
);

CREATE TABLE "PostReactions" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "user_id" INTEGER,
  "reaction_id" INTEGER,
  "post_id" INTEGER,
  FOREIGN KEY(`user_id`) REFERENCES `Users`(`id`),
  FOREIGN KEY(`reaction_id`) REFERENCES `Reactions`(`id`),
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`)
);

CREATE TABLE "Tags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

CREATE TABLE "PostTags" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "post_id" INTEGER,
  "tag_id" INTEGER,
  FOREIGN KEY(`post_id`) REFERENCES `Posts`(`id`),
  FOREIGN KEY(`tag_id`) REFERENCES `Tags`(`id`)
);

CREATE TABLE "Categories" (
  "id" INTEGER PRIMARY KEY AUTOINCREMENT,
  "label" varchar
);

INSERT INTO Categories ('label') VALUES ('News');
INSERT INTO Categories ('label') VALUES ('Lifestyle');
INSERT INTO Categories ('label') VALUES ('Music');
INSERT INTO Categories ('label') VALUES ('Events');
INSERT INTO Categories ('label') VALUES ('Home & Decor');


INSERT INTO Tags ('label') VALUES ('JavaScript');
INSERT INTO Reactions ('label', 'image_url') VALUES ('happy', 'https://pngtree.com/so/happy');

INSERT INTO `Users` VALUES (null, 'Alexis', 'Rose', 'ar@mail.com', 'im a little bit alexis', 'arose', 'alexis', null, 2022-4-24, 1);
INSERT INTO `Users` VALUES (null, 'David', 'Rose', 'dr@mail.com', 'i like the wine not the lable', 'drose', 'david', null, 2022-4-26, 1);

INSERT INTO `Posts` VALUES (null, 1, 1, "live, laugh, love", 2022,'https://images.fastcompany.net/image/upload/w_1280,f_auto,q_auto,fl_lossy/fc/3045872-poster-p-1-justin-lime-timberlake-sauza-901.jpg', "Loving this! saw a bird! so random of me", 1);
INSERT INTO `Posts` VALUES (null, 2, 2, "another bird", 2021,'https://images.fastcompany.net/image/upload/w_1280,f_auto,q_auto,fl_lossy/fc/3045872-poster-p-1-justin-lime-timberlake-sauza-901.jpg', "Wow another bird", 1);

INSERT INTO `Tags` VALUES (null, "Fave Band");
INSERT INTO `Tags` VALUES (null, "Tech News");
INSERT INTO `Tags` VALUES (null, "Mariah Carey");
INSERT INTO `Tags` VALUES (null, "Candles");
INSERT INTO `Tags` VALUES (null, "Thoughts on Life");
INSERT INTO `Tags` VALUES (null, "Dinner Ideas");
INSERT INTO `Tags` VALUES (null, "Daily Musings");



SELECT
            p.id,
            p.user_id,
            p.category_id,
            p.title,
            p.publication_date,
            p.image_url,
            p.content,
            c.label category_label,
            u.first_name user_fn,
            u.last_name user_ln
        FROM Posts p
        JOIN Categories c
            ON c.id = p.category_id
        JOIN Users u
            ON u.id = p.user_id