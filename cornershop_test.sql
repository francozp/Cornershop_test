-- phpMyAdmin SQL Dump
-- version 4.9.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 05, 2019 at 05:56 AM
-- Server version: 10.4.8-MariaDB
-- PHP Version: 7.3.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `cornershop_test`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add main dish', 1, 'add_maindish'),
(2, 'Can change main dish', 1, 'change_maindish'),
(3, 'Can delete main dish', 1, 'delete_maindish'),
(4, 'Can view main dish', 1, 'view_maindish'),
(5, 'Can add menu', 2, 'add_menu'),
(6, 'Can change menu', 2, 'change_menu'),
(7, 'Can delete menu', 2, 'delete_menu'),
(8, 'Can view menu', 2, 'view_menu'),
(9, 'Can add options', 3, 'add_options'),
(10, 'Can change options', 3, 'change_options'),
(11, 'Can delete options', 3, 'delete_options'),
(12, 'Can view options', 3, 'view_options'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add user option', 5, 'add_useroption'),
(18, 'Can change user option', 5, 'change_useroption'),
(19, 'Can delete user option', 5, 'delete_useroption'),
(20, 'Can view user option', 5, 'view_useroption'),
(21, 'Can add log entry', 6, 'add_logentry'),
(22, 'Can change log entry', 6, 'change_logentry'),
(23, 'Can delete log entry', 6, 'delete_logentry'),
(24, 'Can view log entry', 6, 'view_logentry'),
(25, 'Can add permission', 7, 'add_permission'),
(26, 'Can change permission', 7, 'change_permission'),
(27, 'Can delete permission', 7, 'delete_permission'),
(28, 'Can view permission', 7, 'view_permission'),
(29, 'Can add group', 8, 'add_group'),
(30, 'Can change group', 8, 'change_group'),
(31, 'Can delete group', 8, 'delete_group'),
(32, 'Can view group', 8, 'view_group'),
(33, 'Can add user', 9, 'add_user'),
(34, 'Can change user', 9, 'change_user'),
(35, 'Can delete user', 9, 'delete_user'),
(36, 'Can view user', 9, 'view_user'),
(37, 'Can add content type', 10, 'add_contenttype'),
(38, 'Can change content type', 10, 'change_contenttype'),
(39, 'Can delete content type', 10, 'delete_contenttype'),
(40, 'Can view content type', 10, 'view_contenttype'),
(41, 'Can add session', 11, 'add_session'),
(42, 'Can change session', 11, 'change_session'),
(43, 'Can delete session', 11, 'delete_session'),
(44, 'Can view session', 11, 'view_session'),
(45, 'Can add celery taskmeta', 12, 'add_celerytaskmeta'),
(46, 'Can change celery taskmeta', 12, 'change_celerytaskmeta'),
(47, 'Can delete celery taskmeta', 12, 'delete_celerytaskmeta'),
(48, 'Can view celery taskmeta', 12, 'view_celerytaskmeta'),
(49, 'Can add celery tasksetmeta', 13, 'add_celerytasksetmeta'),
(50, 'Can change celery tasksetmeta', 13, 'change_celerytasksetmeta'),
(51, 'Can delete celery tasksetmeta', 13, 'delete_celerytasksetmeta'),
(52, 'Can view celery tasksetmeta', 13, 'view_celerytasksetmeta'),
(53, 'Can add profile', 14, 'add_profile'),
(54, 'Can change profile', 14, 'change_profile'),
(55, 'Can delete profile', 14, 'delete_profile'),
(56, 'Can view profile', 14, 'view_profile'),
(57, 'Can add auth group', 15, 'add_authgroup'),
(58, 'Can change auth group', 15, 'change_authgroup'),
(59, 'Can delete auth group', 15, 'delete_authgroup'),
(60, 'Can view auth group', 15, 'view_authgroup'),
(61, 'Can add auth group permissions', 16, 'add_authgrouppermissions'),
(62, 'Can change auth group permissions', 16, 'change_authgrouppermissions'),
(63, 'Can delete auth group permissions', 16, 'delete_authgrouppermissions'),
(64, 'Can view auth group permissions', 16, 'view_authgrouppermissions'),
(65, 'Can add auth permission', 17, 'add_authpermission'),
(66, 'Can change auth permission', 17, 'change_authpermission'),
(67, 'Can delete auth permission', 17, 'delete_authpermission'),
(68, 'Can view auth permission', 17, 'view_authpermission'),
(69, 'Can add auth user', 18, 'add_authuser'),
(70, 'Can change auth user', 18, 'change_authuser'),
(71, 'Can delete auth user', 18, 'delete_authuser'),
(72, 'Can view auth user', 18, 'view_authuser'),
(73, 'Can add auth user groups', 19, 'add_authusergroups'),
(74, 'Can change auth user groups', 19, 'change_authusergroups'),
(75, 'Can delete auth user groups', 19, 'delete_authusergroups'),
(76, 'Can view auth user groups', 19, 'view_authusergroups'),
(77, 'Can add auth user user permissions', 20, 'add_authuseruserpermissions'),
(78, 'Can change auth user user permissions', 20, 'change_authuseruserpermissions'),
(79, 'Can delete auth user user permissions', 20, 'delete_authuseruserpermissions'),
(80, 'Can view auth user user permissions', 20, 'view_authuseruserpermissions'),
(81, 'Can add django admin log', 21, 'add_djangoadminlog'),
(82, 'Can change django admin log', 21, 'change_djangoadminlog'),
(83, 'Can delete django admin log', 21, 'delete_djangoadminlog'),
(84, 'Can view django admin log', 21, 'view_djangoadminlog'),
(85, 'Can add django content type', 22, 'add_djangocontenttype'),
(86, 'Can change django content type', 22, 'change_djangocontenttype'),
(87, 'Can delete django content type', 22, 'delete_djangocontenttype'),
(88, 'Can view django content type', 22, 'view_djangocontenttype'),
(89, 'Can add django migrations', 23, 'add_djangomigrations'),
(90, 'Can change django migrations', 23, 'change_djangomigrations'),
(91, 'Can delete django migrations', 23, 'delete_djangomigrations'),
(92, 'Can view django migrations', 23, 'view_djangomigrations'),
(93, 'Can add django session', 24, 'add_djangosession'),
(94, 'Can change django session', 24, 'change_djangosession'),
(95, 'Can delete django session', 24, 'delete_djangosession'),
(96, 'Can view django session', 24, 'view_djangosession');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf8_bin NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf8_bin NOT NULL,
  `first_name` varchar(30) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(150) COLLATE utf8_bin NOT NULL,
  `email` varchar(254) COLLATE utf8_bin NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(19, 'pbkdf2_sha256$150000$S282Ms3qroDq$dCit+foysgL4UIF9ELeH6xk0VO/wPk4H7WGqQelSvnQ=', '2019-11-05 04:50:18.104336', 0, 'nora', '', '', '', 0, 1, '2019-11-04 03:05:32.479043');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `celery_taskmeta`
--

CREATE TABLE `celery_taskmeta` (
  `id` int(11) NOT NULL,
  `task_id` varchar(255) COLLATE utf8_bin NOT NULL,
  `status` varchar(50) COLLATE utf8_bin NOT NULL,
  `result` longtext COLLATE utf8_bin DEFAULT NULL,
  `date_done` datetime(6) NOT NULL,
  `traceback` longtext COLLATE utf8_bin DEFAULT NULL,
  `hidden` tinyint(1) NOT NULL,
  `meta` longtext COLLATE utf8_bin DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `celery_tasksetmeta`
--

CREATE TABLE `celery_tasksetmeta` (
  `id` int(11) NOT NULL,
  `taskset_id` varchar(255) COLLATE utf8_bin NOT NULL,
  `result` longtext COLLATE utf8_bin NOT NULL,
  `date_done` datetime(6) NOT NULL,
  `hidden` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf8_bin DEFAULT NULL,
  `object_repr` varchar(200) COLLATE utf8_bin NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf8_bin NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf8_bin NOT NULL,
  `model` varchar(100) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(6, 'admin', 'logentry'),
(8, 'auth', 'group'),
(7, 'auth', 'permission'),
(9, 'auth', 'user'),
(10, 'contenttypes', 'contenttype'),
(15, 'csweb', 'authgroup'),
(16, 'csweb', 'authgrouppermissions'),
(17, 'csweb', 'authpermission'),
(18, 'csweb', 'authuser'),
(19, 'csweb', 'authusergroups'),
(20, 'csweb', 'authuseruserpermissions'),
(12, 'csweb', 'celerytaskmeta'),
(13, 'csweb', 'celerytasksetmeta'),
(21, 'csweb', 'djangoadminlog'),
(22, 'csweb', 'djangocontenttype'),
(23, 'csweb', 'djangomigrations'),
(24, 'csweb', 'djangosession'),
(1, 'csweb', 'maindish'),
(2, 'csweb', 'menu'),
(3, 'csweb', 'options'),
(14, 'csweb', 'profile'),
(4, 'csweb', 'user'),
(5, 'csweb', 'useroption'),
(11, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) COLLATE utf8_bin NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-11-01 02:35:40.823516'),
(2, 'auth', '0001_initial', '2019-11-01 02:35:40.922452'),
(3, 'admin', '0001_initial', '2019-11-01 02:35:41.380955'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-11-01 02:35:41.479248'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-11-01 02:35:41.488239'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-11-01 02:35:41.551949'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-11-01 02:35:41.599207'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-11-01 02:35:41.658497'),
(9, 'auth', '0004_alter_user_username_opts', '2019-11-01 02:35:41.666373'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-11-01 02:35:41.718497'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-11-01 02:35:41.728150'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-11-01 02:35:41.736100'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-11-01 02:35:41.756048'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-11-01 02:35:41.774996'),
(15, 'auth', '0010_alter_group_name_max_length', '2019-11-01 02:35:41.832914'),
(16, 'auth', '0011_update_proxy_permissions', '2019-11-01 02:35:41.841910'),
(17, 'csweb', '0001_initial', '2019-11-01 02:35:41.849888'),
(18, 'sessions', '0001_initial', '2019-11-01 02:35:41.868838'),
(19, 'csweb', '0002_auto_20191031_2335', '2019-11-01 02:36:24.985764'),
(20, 'csweb', '0003_authgroup_authgrouppermissions_authpermission_authuser_authusergroups_authuseruserpermissions_django', '2019-11-04 23:00:48.130176'),
(21, 'csweb', '0004_auto_20191104_2001', '2019-11-04 23:01:51.082741');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf8_bin NOT NULL,
  `session_data` longtext COLLATE utf8_bin NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('5ukyq0vrjfvma2lx8vgqktm3nxdw8jjz', 'ZjU2YTFmYTNlZDVkNjMwM2M5OGM2Y2VlNTg2OGRiZDkxMWFiNWNkZTp7Il9hdXRoX3VzZXJfaWQiOiIxNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYWY5OTNiYmUzYjkwYzcyYjA0ZTJiYTliNTMzZmFlMTk2MWY1MGY3MCJ9', '2019-11-15 22:34:14.360882'),
('9cbx6mytnt98zdk07fdxwil9kq6vkrlv', 'ZjU2YTFmYTNlZDVkNjMwM2M5OGM2Y2VlNTg2OGRiZDkxMWFiNWNkZTp7Il9hdXRoX3VzZXJfaWQiOiIxNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYWY5OTNiYmUzYjkwYzcyYjA0ZTJiYTliNTMzZmFlMTk2MWY1MGY3MCJ9', '2019-11-18 00:57:12.760579'),
('yo8ekamloloii082u3vdhcp1vnpqbder', 'ZjU2YTFmYTNlZDVkNjMwM2M5OGM2Y2VlNTg2OGRiZDkxMWFiNWNkZTp7Il9hdXRoX3VzZXJfaWQiOiIxNCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYWY5OTNiYmUzYjkwYzcyYjA0ZTJiYTliNTMzZmFlMTk2MWY1MGY3MCJ9', '2019-11-16 17:04:21.131265');

-- --------------------------------------------------------

--
-- Table structure for table `main_dish`
--

CREATE TABLE `main_dish` (
  `main_id` varchar(36) COLLATE utf8_bin NOT NULL,
  `description` text COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `main_dish`
--

INSERT INTO `main_dish` (`main_id`, `description`) VALUES
('142dc590-5571-4a76-8bd5-76cd15a23160', 'Papilote'),
('186feb23-efcf-44d9-8cbc-50444f220a8d', 'Sushi'),
('24a39d2e-577a-440c-af65-b2c1f9ae3b99', 'Cazuela'),
('3559b202-d775-4739-98c1-5cefe05c9d12', 'Risotto'),
('379223e0-936f-4ef2-acaf-4d0dab6efda0', 'Charquican'),
('38e471d4-e172-4369-8218-a639b302336b', 'Ensalada Cesar'),
('4ce9a4f1-0c9f-49af-8a4d-ddf535083242', 'Arroz con hamburguesa'),
('7cc9d647-dde1-44ae-a952-8388f7f4a153', 'Pastel de choclo'),
('7f14a2e4-f42e-4d0d-9276-4810483ff035', 'Porotos con rienda'),
('a089bbb3-1556-43d4-991f-ca50fa972beb', 'Lasagna'),
('a2693594-75fd-4b35-b7d6-f59f8b035c9c', 'Vienesas con puré'),
('bcf892be-8062-43ac-9443-5a8d0e4c1910', 'Humitas'),
('e6dcfddd-2ae6-4a3f-aff9-3545b0305e17', 'Arroz con nugget de pollo'),
('ed84bc91-27f1-4f74-af4c-93f12ca84daa', 'Ensalada premium de pollo');

-- --------------------------------------------------------

--
-- Table structure for table `menu`
--

CREATE TABLE `menu` (
  `menu_id` varchar(36) COLLATE utf8_bin NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `menu`
--

INSERT INTO `menu` (`menu_id`, `fecha`) VALUES
('384543d7-4b08-4875-af3e-337ffd9e0f9c', '2019-11-05');

-- --------------------------------------------------------

--
-- Table structure for table `options`
--

CREATE TABLE `options` (
  `option_id` varchar(36) COLLATE utf8_bin NOT NULL,
  `main_id` varchar(36) COLLATE utf8_bin NOT NULL,
  `menu_id` varchar(36) COLLATE utf8_bin NOT NULL,
  `salad` tinyint(1) NOT NULL,
  `dessert` tinyint(1) NOT NULL,
  `menu_option` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `options`
--

INSERT INTO `options` (`option_id`, `main_id`, `menu_id`, `salad`, `dessert`, `menu_option`) VALUES
('914b3014-5d00-4e59-b5fe-ce1f34a305d2', '379223e0-936f-4ef2-acaf-4d0dab6efda0', '384543d7-4b08-4875-af3e-337ffd9e0f9c', 1, 1, 1),
('974a1b28-2d90-4f8e-b22e-8b6aeccfe915', '24a39d2e-577a-440c-af65-b2c1f9ae3b99', '384543d7-4b08-4875-af3e-337ffd9e0f9c', 0, 1, 2),
('a80c347f-0024-49fc-8a1b-c5319b665459', '4ce9a4f1-0c9f-49af-8a4d-ddf535083242', '384543d7-4b08-4875-af3e-337ffd9e0f9c', 1, 1, 3);

-- --------------------------------------------------------

--
-- Table structure for table `profile`
--

CREATE TABLE `profile` (
  `user_id` int(11) NOT NULL,
  `privileges` tinyint(1) NOT NULL,
  `name` varchar(100) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `profile`
--

INSERT INTO `profile` (`user_id`, `privileges`, `name`) VALUES
(19, 1, 'Nora');

-- --------------------------------------------------------

--
-- Table structure for table `user_option`
--

CREATE TABLE `user_option` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `option_id` varchar(36) COLLATE utf8_bin NOT NULL,
  `detail` text COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Dumping data for table `user_option`
--

INSERT INTO `user_option` (`id`, `user_id`, `option_id`, `detail`) VALUES
(16, 19, '914b3014-5d00-4e59-b5fe-ce1f34a305d2', 'Con huevo frito encima');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `celery_taskmeta`
--
ALTER TABLE `celery_taskmeta`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `task_id` (`task_id`),
  ADD KEY `celery_taskmeta_hidden_23fd02dc` (`hidden`);

--
-- Indexes for table `celery_tasksetmeta`
--
ALTER TABLE `celery_tasksetmeta`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `taskset_id` (`taskset_id`),
  ADD KEY `celery_tasksetmeta_hidden_593cfc24` (`hidden`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `main_dish`
--
ALTER TABLE `main_dish`
  ADD PRIMARY KEY (`main_id`);

--
-- Indexes for table `menu`
--
ALTER TABLE `menu`
  ADD PRIMARY KEY (`menu_id`);

--
-- Indexes for table `options`
--
ALTER TABLE `options`
  ADD PRIMARY KEY (`option_id`),
  ADD KEY `main` (`main_id`),
  ADD KEY `menu` (`menu_id`);

--
-- Indexes for table `profile`
--
ALTER TABLE `profile`
  ADD PRIMARY KEY (`user_id`);

--
-- Indexes for table `user_option`
--
ALTER TABLE `user_option`
  ADD PRIMARY KEY (`id`),
  ADD KEY `options` (`option_id`),
  ADD KEY `user` (`user_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=23;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `celery_taskmeta`
--
ALTER TABLE `celery_taskmeta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `celery_tasksetmeta`
--
ALTER TABLE `celery_tasksetmeta`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `user_option`
--
ALTER TABLE `user_option`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `options`
--
ALTER TABLE `options`
  ADD CONSTRAINT `main` FOREIGN KEY (`main_id`) REFERENCES `main_dish` (`main_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `menu` FOREIGN KEY (`menu_id`) REFERENCES `menu` (`menu_id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `profile`
--
ALTER TABLE `profile`
  ADD CONSTRAINT `user_profile` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `user_option`
--
ALTER TABLE `user_option`
  ADD CONSTRAINT `options` FOREIGN KEY (`option_id`) REFERENCES `options` (`option_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `user` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
