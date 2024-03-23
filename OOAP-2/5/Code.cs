﻿// Как мне кажется, язык C# поддерживает все пять принципов повторного использования модуля:
// 1) в языке есть типы-дженерики
// 2, 3) модуль может объединять несколько функций и может входить в семейство модулей (библиотека), и мне сложно представить ситуацию, когда это не так.
// 4) Модуль может представлять конкретную реализацию родительского модуля, и может выбираться динамически во время выполнения (вроде бы в C# даже multiple dispatch можно эмулировать)
// 5) Модуль может интегрировать общее поведение нескольких похожих модулей, предоставив общий интерфейс и скрытно определяя какому конкретно модулю нужно делегировать выполнение вызова.