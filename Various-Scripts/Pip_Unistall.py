import subprocess
import sys

# Скрипт удаляет установленные модули Python с использованием pip.
# Получение списка пакетов осуществляется через команду pip list.
# Критически важные модули (pip, setuptools, wheel) защищены от удаления.
# Скрипт выводит список модулей, которые планируется удалить, а также отображает статус удаления каждого модуля.
# После выполнения удалений выводится количество успешно удалённых модулей.
# Скрипт поддерживает автоматическую установку недостающих библиотек, если это необходимо.
# Для предотвращения автоматического закрытия окна, после завершения работы скрипт ожидает нажатия Enter.

# The script removes installed Python modules using pip.
# It retrieves the list of packages via the pip list command.
# Critical modules (pip, setuptools, wheel) are protected from removal.
# The script displays the list of modules scheduled for removal and shows the removal status for each module.
# After completing the removal process, the number of successfully removed modules is displayed.
# The script supports automatic installation of missing libraries if necessary.
# To prevent the window from closing automatically, the script waits for the Enter key to be pressed after finishing.

def get_installed_packages():
    """Получает список всех установленных пакетов через pip."""
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "list", "--format=freeze"], 
                                capture_output=True, text=True, check=True)
        packages = result.stdout.splitlines()
        # Каждый пакет выглядит как "package_name==version", берем только имена
        return [pkg.split("==")[0] for pkg in packages]
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving the package list: {e}")
        return []

def uninstall_packages(packages):
    """Удаляет список пакетов и возвращает количество успешно удаленных."""
    removed_count = 0
    for package in packages:
        print(f"Uninstalling package: {package}...")
        try:
            # Удаляем пакет
            subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", package], 
                           check=True)
            removed_count += 1
        except subprocess.CalledProcessError as e:
            print(f"Failed to uninstall {package}: {e}")
    return removed_count

def main():
    try:
        # Получаем список всех установленных пакетов
        print("Retrieving the list of installed packages...")
        installed_packages = get_installed_packages()

        # Если список пакетов пуст, завершаем работу с сообщением
        if not installed_packages:
            print("No installed packages found or unable to retrieve package list.")
            input("Press Enter to exit...")
            return

        # Исключаем критически важные пакеты
        critical_packages = {'pip', 'setuptools', 'wheel'}
        packages_to_uninstall = [pkg for pkg in installed_packages if pkg not in critical_packages]

        if not packages_to_uninstall:
            print("No packages to uninstall.")
            input("Press Enter to exit...")
            return

        print(f"\nTotal packages found for uninstallation: {len(packages_to_uninstall)}")
        print("Packages scheduled for uninstallation:")
        print("\n".join(packages_to_uninstall))

        # Удаляем пакеты
        removed_count = uninstall_packages(packages_to_uninstall)

        # Итоговая информация
        print(f"\nNumber of packages uninstalled: {removed_count}/{len(packages_to_uninstall)}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Оставляем окно открытым
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()