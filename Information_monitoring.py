# Information_monitoring.py

import re
import time
import copy
from typing import Dict, List, Any, Optional, Tuple
from collections import deque
# استيراد الأدوات السيادية التي رفعتها
from P1_sovereign_utils import SovereignSupervisorySystem, profile_performance


class SovereignCloner:
    """
    [CLONING ENGINE V1.0]: محرك الاستنساخ الإدراكي.
    يعمل كآلية كاتبة تنسخ المستندات مع الحفاظ على الأصول في الذاكرة.
    """
    def __init__(self):
        # الذاكرة المؤقتة الدائمة (الخزنة للأصول)
        self._immutable_vault = {}
        # الذاكرة النشطة (النسخ قيد الاستخدام)
        self.active_workspace = {}

        # تفعيل نظام الرقابة السيادي داخل المحرك
        self.logger = SovereignSupervisorySystem("CLONER_CORE")

    @profile_performance
    def process_and_clone(self, file_id: str, content: Any) -> Dict[str, Any]:
        """
        [THE SUPERVISED TYPEWRITER]:
        نسخ ورصد مع تسجيل كامل للعمليات في سجل الحوادث والرقابة.
        """
        self.logger.info(f"🚀 بدء عملية الاستنساخ الإدراكي للملف: {file_id}")

        # المرحلة 1: التأمين في الخزنة
        self._immutable_vault[file_id] = {
            "original_data": content,
            "timestamp": time.time(),
            "status": "LOCKED"
        }

        # المرحلة 2: الرصد والنسخ اليدوي (أحرف + صور)
        reconstructed_data = ""
        visual_map = []
        raw_stream = str(content)

        # رادار الصور والإحداثيات
        image_patterns = r"(?P<name>[\w\-_]+\.(png|jpg|jpeg|gif))|(?P<coord>rect\([\d,\s]+\))"

        try:
            for match in re.finditer(image_patterns, raw_stream, re.IGNORECASE):
                image_info = {
                    "asset": match.group("name"),
                    "coord": match.group("coord"),
                    "index": match.start()
                }
                visual_map.append(image_info)
                # تسجيل اكتشاف صورة كحدث في الرقابة
                if image_info["asset"]:
                    self.logger.debug(f"📸 تم رصد صورة: {image_info['asset']} عند الموقع {image_info['index']}")

            # رصد الإشارات النصية (النبضة الإدراكية)
            sensory_pulse = self.sense_signal(raw_stream, deque(maxlen=5))

            # اللصق في الذاكرة النشطة
            reconstructed_data = raw_stream

            # المرحلة 3: التشفير النهائي في الوعي
            active_copy = {
                "data": reconstructed_data,
                "sensory_intelligence": {
                    "text_signals": sensory_pulse,
                    "visual_assets": visual_map,
                    "is_conscious": sensory_pulse["is_conscious"] or len(visual_map) > 0
                },
                "metadata": {
                    "source_id": file_id,
                    "version": "SOVEREIGN_V5_AUDITED",
                    "cloned_at": time.time()
                }
            }

            self.active_workspace[file_id] = active_copy

            if active_copy["sensory_intelligence"]["is_conscious"]:
                self.logger.info(f"🧠 [CONSCIOUS]: الملف {file_id} سجل نبضة إدراكية عالية.")

            return active_copy

        except Exception as e:
            # تسجيل الحادثة فوراً في نظام الرقابة السيادي
            self.logger.error(f"❌ فشل في استنساخ الملف {file_id}: {str(e)}")
            return {}

    def sense_signal(self, raw_stream: str, current_context_window: deque) -> Dict[str, Any]:
        """دالة الرصد الحسي التي قمت بتطويرها"""
        signal_patterns = {
            "kinematic": r"(θ|τ|deg|rad|link|joint|arm)",
            "dynamic": r"(mass|torque|inertia|force|gravity)",
            "structural": r"(matrix|transform|jacobian|vector|eigen)"
        }
        detected_frequencies = [tag for tag, pat in signal_patterns.items() if re.search(pat, raw_stream, re.IGNORECASE)]

        # حساب الرنين والنبضة (من كودك الأصلي)
        spike_intensity = len(detected_frequencies) * 5.0 # تبسيط للحساب

        return {
            "perceptual_spike": round(spike_intensity, 2),
            "signals": detected_frequencies,
            "is_conscious": spike_intensity > 10.0,
            "timestamp": time.time()
        }

    def finalize_session(self):
        """إغلاق المحرك واستخراج ملخص الرقابة"""
        summary = self.logger.get_audit_summary()
        self.logger.info(f"📊 ملخص الجلسة: {summary}")
        self.logger.shutdown_sequence()

    def sense_signal(self, raw_stream: str, current_context_window: deque) -> Dict[str, Any]:
        """
        [SENSORY MONITOR V1.0]: دالة الرصد الحسي للمعلومات.
        تحول النص الخام إلى 'نبضة إدراكية' بناءً على الرنين مع الذاكرة السياقية.
        """

        # 1. المرحلة الحسية: استخراج "البصمة الترددية" (Patterns)
        # لا نبحث عن كلمات فقط، بل عن "هياكل" (رموز رياضية، قيم عددية، علاقات)
        signal_patterns = {
            "kinematic": r"(θ|τ|deg|rad|link|joint|arm)",
            "dynamic": r"(mass|torque|inertia|force|gravity)",
            "structural": r"(matrix|transform|jacobian|vector|eigen)"
        }

        detected_frequencies = []
        for tag, pattern in signal_patterns.items():
            if re.search(pattern, raw_stream, re.IGNORECASE):
                detected_frequencies.append(tag)

        # 2. استدعاء الذاكرة السياقية (Contextual Resonance)
        # فحص "الرنين" مع آخر 5 أحداث في الذاكرة لرفع درجة الإدراك
        resonance_factor = 1.0
        for past_event in list(current_context_window)[-5:]:
            # إذا كان هناك تطابق في التردد بين الماضي والحاضر، يحدث "رنين" (Resonance)
            shared_signals = set(detected_frequencies) & set(past_event.get('signals', []))
            resonance_score = len(shared_signals) * 1.5
            resonance_factor += resonance_score

        # 3. حساب "النبضة الإدراكية" (Perceptual Spike)
        # شدة النبضة تعتمد على وجود المعلومات + الرنين مع السياق
        spike_intensity = (len(detected_frequencies) * 2.0) * resonance_factor

        # 4. الترميز الحسي النهائي (Sensory Encoding)
        sensory_code = {
            "perceptual_spike": round(spike_intensity, 2),
            "signals": detected_frequencies,
            "is_conscious": spike_intensity > 15.0, # هل المعلومة تستحق الانتقال للوعي؟
            "timestamp": time.time()
        }

        return sensory_code


class PerceptualPerceptionEngine:
    """
    [PERCEPTUAL ENGINE V1.0]:
    نظام إدراك حسي يعتمد على الترميز النبضي والتغذية السياقية.
    """
    def __init__(self, memory_size: int = 100):
        # الذاكرة السياقية المؤقتة (تخزن بصمات الأحداث الأخيرة)
        self.contextual_memory = deque(maxlen=memory_size)
        # مصفوفة الأوزان الإدراكية (Sensory Weights)
        self.perceptual_weights = {}

    @profile_performance
    def sense_and_encode(self, raw_input: str, sensory_schema: str) -> Dict[str, Any]:
        """
        [THE DIPLOMATIC ENCODER]:
        تحويل المدخلات الخام إلى كود حسي عبر إدارة متوازنة للدوال المساعدة وتوافق مع آلية الاستنساخ.
        """
        # 1. المرحلة الدبلوماسية الأولى: التحقق والاستخراج اللطيف
        # نضمن أن المدخلات نصية لتجنب كسر دالة التوقيع الترددي
        safe_input = str(raw_input) if raw_input else ""

        # استدعاء الدالة الأصلية لاستخراج الترددات
        frequency_signature = self._extract_frequency_signature(safe_input)

        # 2. المرحلة الدبلوماسية الثانية: تقييم الرنين السياقي
        # إذا كانت الترددات فارغة، نتعامل معها كـ "نبضة هادئة" دون توقف النظام
        if not frequency_signature:
            self.logger.warning(f"⚠️ [SENSE]: لم يتم رصد ترددات واضحة في الوسم {sensory_schema}")
            perception_intensity = 1.0 # إدراك أساسي محايد
        else:
            # استدعاء الدالة الأصلية لحساب الرنين بناءً على الذاكرة السياقية
            perception_intensity = self._calculate_resonance(frequency_signature)

        # 3. المرحلة الدبلوماسية الثالثة: الترميز المتوافق (The Perceptual Encoding)
        # نستخدم np.datetime64 لضمان دقة الطابع الزمني كما في التصميم الأصلي
        perceptual_code = {
            "signature": frequency_signature,
            "intensity": perception_intensity,
            "schema_tag": sensory_schema,
            "timestamp": np.datetime64('now'),
            "is_conscious": perception_intensity > 2.0 # عتبة وعي دبلوماسية
        }

        # 4. التغذية الراجعة وتحديث الذاكرة
        # نغذي الذاكرة السياقية فوراً لرفع الوعي اللحظي للعمليات القادمة
        self.contextual_memory.append(perceptual_code)

        # 5. التوافق مع process_and_clone:
        # نقوم بإرسال إشارة للمراقب إذا كانت النبضة تتطلب "انتباه" المحرك السيادي
        if perceptual_code["is_conscious"]:
            self.logger.info(f"✨ [DIPLOMAT]: رصد رنين عالي ({perception_intensity}) تحت وسم {sensory_schema}")

        return perceptual_code

    def bridge_to_perception(self, file_id: str, perception_engine: 'PerceptualPerceptionEngine') -> Dict[str, Any]:
        """
        [THE PERCEPTUAL BRIDGE]:
        دالة مساعدة تربط نواتج عملية النسخ (process_and_clone) بالمحرك الإدراكي.
        تضمن تحويل البيانات المنسوخة يدويًا إلى أكواد حسية مشفرة.
        """
        # 1. استخراج البيانات من بيئة العمل النشطة (التي تم بناؤها في process_and_clone)
        active_data = self.active_workspace.get(file_id)
        if not active_data:
            self.logger.error(f"❌ فشل الجسر: لا توجد بيانات نشطة للملف {file_id}")
            return {}

        # 2. تحضير "المدخل الخام" من النصوص المنسوخة والصور المرصودة
        # ندمج إشارات النصوص مع بيانات الأصول البصرية المكتشفة
        reconstructed_text = active_data.get("data", "")
        visual_assets = active_data.get("sensory_intelligence", {}).get("visual_assets", [])

        # إنشاء وسم حسي مخصص بناءً على نوع الملف أو المحتوى المرصود
        schema_tag = "ROBOTICS_TECHNICAL" if "sensory_intelligence" in active_data else "GENERAL_DATA"

        # 3. استدعاء المحرك الإدراكي لتشفير "النبضة" (Sense and Encode)
        # نمرر النص المعاد بناؤه للمحرك لكي يحسب الرنين السياقي
        perceptual_code = perception_engine.sense_and_encode(
            raw_input=reconstructed_text,
            sensory_schema=schema_tag
        )

        # 4. دمج الكود الحسي المشفر مع النسخة النشطة للملف
        # الآن تصبح النسخة النشطة تحتوي على "البيانات" + "التشفير الإدراكي"
        active_data["perceptual_encoding"] = perceptual_code
        active_data["metadata"]["encoded_at"] = time.time()

        self.logger.info(f"⚡ [BRIDGE]: تم تشفير الملف {file_id} إدراكيًا بشدة: {perceptual_code['intensity']}")

        return perceptual_code

    def _calculate_resonance(self, current_signature: List[str]) -> float:
        """
        حساب الرنين: هل المعلومة الحالية "مألوفة" أو "مكملة" لما في الذاكرة؟
        """
        if not self.contextual_memory:
            return 1.0  # إدراك أساسي

        resonance_score = 1.0
        # فحص آخر 10 نبضات في الذاكرة السياقية
        recent_memory = list(self.contextual_memory)[-10:]

        for past_code in recent_memory:
            # إذا كانت الكلمات تتكرر، يزداد "الرنين الإدراكي" (تصبح المعلومة حساسة)
            common_elements = set(current_signature) & set(past_code['signature'])
            resonance_score += (len(common_elements) * 0.5)

        return resonance_score

    def _extract_frequency_signature(self, text: str) -> List[str]:
        # استخراج العناصر التي تمثل "هوية" النص التقنية
        return re.findall(r'\b\w{4,}\b', text.lower()) # كمثال عام
