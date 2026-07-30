#include <jni.h>
#include <string>

extern "C" JNIEXPORT jstring JNICALL
Java_id_web_app_onlinecbt_MainActivity_stringFromJNI(
        JNIEnv* env,
        jobject /* this */) {
    std::string hello = "Hello from C++ Native!";
    return env->NewStringUTF(hello.c_str());
}

extern "C" JNIEXPORT jboolean JNICALL
Java_id_web_app_onlinecbt_MainActivity_checkLicense(
        JNIEnv* env,
        jobject /* this */) {
    return JNI_TRUE; // Always return true (bypass)
}
