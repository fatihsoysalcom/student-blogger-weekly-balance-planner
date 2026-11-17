import collections
from dataclasses import dataclass

# Define a simple Task structure using dataclass
@dataclass
class Task:
    name: str
    category: str # e.g., 'Akademik', 'Blog', 'Kişisel'
    estimated_hours: int
    priority: str # e.g., 'High', 'Medium', 'Low'

# Priority mapping for sorting
PRIORITY_MAP = {'High': 3, 'Medium': 2, 'Low': 1}

def generate_weekly_plan(tasks):
    """
    Generates a conceptual weekly plan, prioritizing tasks and summarizing
    time allocation across different categories.
    """
    print("--- Öğrenci Blog Yazarı Haftalık Planlayıcı ---") # Student Blogger Weekly Planner
    print("--- Student Blogger Weekly Planner ---")
    print("\nAmacımız: Akademik ve Blog görevlerini dengelemek.") # Goal: Balance Academic and Blog tasks.
    print("Goal: Balance Academic and Blog tasks.\n")

    # Sort tasks by priority (descending) and then by estimated hours (descending)
    # This ensures higher priority tasks are considered first.
    # Bu, yüksek öncelikli görevlerin önce ele alınmasını sağlar.
    sorted_tasks = sorted(
        tasks,
        key=lambda t: (PRIORITY_MAP.get(t.priority, 0), t.estimated_hours),
        reverse=True
    )

    print("Önceliklendirilmiş Görev Listesi (Proposed Prioritized Task List):\n")
    for i, task in enumerate(sorted_tasks):
        print(f"{i+1}. [{task.priority}] {task.name} ({task.category}, {task.estimated_hours} saat)")
        # Bu kısım, farklı görev türlerini (Akademik, Blog, Kişisel) öncelik sırasına göre düzenler.
        # This section organizes different task types (Academic, Blog, Personal) by priority.


    # Calculate total hours for each category
    # Her kategori için toplam saatleri hesapla
    category_hours = collections.defaultdict(int)
    total_productive_hours = 0

    for task in sorted_tasks:
        category_hours[task.category] += task.estimated_hours
        total_productive_hours += task.estimated_hours
        # Bu kısım, akademik ve blog görevleri gibi farklı alanlara ayrılan zamanı göstererek dengeyi görselleştirir.
        # This section visualizes the balance by showing time allocated to different areas like academic and blog tasks.


    print("\n--- Haftalık Zaman Dağılımı Özeti (Weekly Time Allocation Summary) ---\n")
    for category, hours in category_hours.items():
        print(f"{category} Görevleri: {hours} saat") # Category Tasks: X hours
    print(f"\nToplam Planlanan Üretken Saat: {total_productive_hours} saat") # Total Planned Productive Hours

    # Simple feedback on balance
    academic_h = category_hours.get('Akademik', 0)
    blog_h = category_hours.get('Blog', 0)

    print("\n--- Denge Analizi (Balance Analysis) ---")
    if academic_h > blog_h * 2 and academic_h > 0:
        print("İpucu: Akademik görevlere çok fazla odaklanmışsınız gibi görünüyor. Blog içeriğinize daha fazla zaman ayırmayı düşünebilirsiniz!")
        print("Tip: You seem heavily focused on academic tasks. Consider dedicating more time to your blog content!")
    elif blog_h > academic_h * 2 and blog_h > 0:
        print("İpucu: Blog görevlerine çok fazla odaklanmışsınız gibi görünüyor. Akademik başarı için derslerinize daha fazla zaman ayırmayı unutmayın!")
        print("Tip: You seem heavily focused on blog tasks. Don't forget to dedicate more time to your studies for academic success!")
    elif academic_h > 0 and blog_h > 0 and abs(academic_h - blog_h) <= max(academic_h, blog_h) * 0.5:
        print("Harika iş! Akademik ve blog görevleriniz arasında iyi bir denge kurmuşsunuz.")
        print("Great job! You've established a good balance between your academic and blog tasks.")
    else:
        print("Planınızda akademik ve blog görevlerinin dengesini gözden geçirin.")
        print("Review the balance of academic and blog tasks in your plan.")

    print("\nBu plan, haftalık hedeflerinizi belirlemenize ve zamanınızı daha verimli yönetmenize yardımcı olmayı amaçlar.")
    print("This plan aims to help you set weekly goals and manage your time more efficiently.")


if __name__ == "__main__":
    # Example tasks for a student blogger
    # Öğrenci blog yazarı için örnek görevler
    student_tasks = [
        Task("Matematik Ödevi", "Akademik", 5, "High"),
        Task("Proje Araştırması", "Akademik", 8, "High"),
        Task("Sınav Çalışması (Veri Yapıları)", "Akademik", 10, "High"),
        Task("Yeni Blog Yazısı Taslağı (Teknik Konu)", "Blog", 6, "Medium"),
        Task("Eski Yazıyı Güncelleme ve SEO Optimizasyonu", "Blog", 3, "Low"),
        Task("Sosyal Medya Tanıtımı", "Blog", 2, "Low"),
        Task("Blog İçin Konu Beyin Fırtınası", "Blog", 1, "Medium"),
        Task("Arkadaşlarla Buluşma", "Kişisel", 4, "Low"),
        Task("Spor Salonu", "Kişisel", 3, "Medium"),
        Task("Online Kurs (Yeni Dil)", "Kişisel", 2, "Low"),
    ]

    generate_weekly_plan(student_tasks)
