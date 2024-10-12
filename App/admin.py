from django.contrib import admin
from .models import (
    Todo,
    UserProfile,
    Department,
    Student,
    Faculty,
    Course,
    Enrollment,
    Exam,
    Grade,
    Event,
    LibraryResource,
    Attendance,
    Group,
    Chat,
    FriendRequest,
)

@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'completed', 'create_at', 'author')
    search_fields = ('title', 'description')
    list_filter = ('completed', 'create_at')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio')
    search_fields = ('user__username',)

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'building', 'head')
    search_fields = ('name',)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'enrollment_number', 'department', 'date_of_birth')
    search_fields = ('user__first_name', 'user__last_name', 'enrollment_number')

@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('user', 'employee_id', 'department', 'designation')
    search_fields = ('user__first_name', 'user__last_name', 'employee_id')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'department', 'credits')
    search_fields = ('code', 'name')

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'semester', 'date_enrolled')
    search_fields = ('student__user__first_name', 'course__name')

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('course', 'exam_date', 'exam_type')
    search_fields = ('course__name', 'exam_type')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'grade')
    search_fields = ('student__user__first_name', 'exam__course__name')

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')
    search_fields = ('title',)

@admin.register(LibraryResource)
class LibraryResourceAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'isbn', 'category', 'available_copies')
    search_fields = ('title', 'author', 'isbn')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'status')
    search_fields = ('student__user__first_name', 'course__name')

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at')
    search_fields = ('name',)

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'group', 'message_type', 'created_at')
    search_fields = ('sender__user__username', 'receiver__user__username')

@admin.register(FriendRequest)
class FriendRequestAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'created_at')
    search_fields = ('from_user__user__username', 'to_user__user__username')

