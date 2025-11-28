### 1. Задание

Как при помощи Pypyr сохранить относительные пути при конвертации Stylus в CSS?

### 2. MCVE

Я имею следующую структуру папок:

```text
C:\PROJECTS\SASHATRAVIS\OUTPUT
\---theme
    \---stylus
        +---KiraFirstFolder
        |       KiraFirstFile.styl
        |
        \---KiraSecondFolder
            |   KiraSecondFile.styl
            |
            \---KiraSubfolder
                    KiraThirdFile.styl
```

Я желаю, чтобы Stylus одной командой сконвертировал файлы из папки `stylus` в папку `css` следующим образом:

```text
C:\PROJECTS\SASHATRAVIS\OUTPUT
\---theme
    +---css
    |   +---KiraFirstFolder
    |   |       KiraFirstFile.css
    |   |
    |   \---KiraSecondFolder
    |       |   KiraSecondFile.css
    |       |
    |       \---KiraSubfolder
    |               KiraThirdFile.css
    |
    \---stylus
        +---KiraFirstFolder
        |       KiraFirstFile.styl
        |
        \---KiraSecondFolder
            |   KiraSecondFile.styl
            |
            \---KiraSubfolder
                    KiraThirdFile.styl
```

Как если бы пользователь запустил 3 команды:

```sh
# [INFO] Stylus CLI usage:
# https://stylus-lang.com/docs/executable.html#compiling-files-example
- stylus output/theme/stylus/KiraFirstFolder/KiraFirstFile.styl --out output/theme/css/KiraFirstFolder/KiraFirstFile.css
- stylus output/theme/stylus/KiraSecondFolder/KiraSecondFile.styl --out output/theme/css/KiraSecondFolder/KiraSecondFile.css
- stylus output/theme/stylus/KiraSecondFolder/KiraSubfolder/KiraThirdFile.styl --out output/theme/css/KiraSecondFolder/KiraSubfolder/KiraThirdFile.css
```

Как это сделать, используя Pypyr?

### 3. Неудачные решения

Мой файл `StylusReldir.yaml`:

```yaml
steps:
- in:
    glob: output/theme/stylus/**/*.styl
  name: pypyr.steps.glob

- foreach: "{globOut}"
  in:
    cmd: stylus {i} --out output/theme/css
  name: pypyr.steps.shell

```

После запуска команды `pypyr StylusReldir` Pypyr сохранил `.css`-файлы в папке `css`, не сохранив структуру. Как я могу исправить файл `StylusReldir.yaml`, чтобы получить желаемое поведение?

### 4. Источники

Перед ответом, пожалуйста, просмотрите:

1. [**Документацию к Pypyr**](https://pypyr.io/docs/).
1. [**Исходный код Pypyr**](https://github.com/pypyr/pypyr/).
1. [**Issues**](https://github.com/pypyr/pypyr/issues) и [**дискуссии**](https://github.com/pypyr/pypyr/discussions) Pypyr.

### 5. Проверка

Пожалуйста, если Вы нашли решение, запускайте команду `pypyr StylusReldir` и проверяйте папки, куда сохранились выходные файлы.

Пожалуйста, выводите комментарии и ответ на русском языке.

Спасибо.
