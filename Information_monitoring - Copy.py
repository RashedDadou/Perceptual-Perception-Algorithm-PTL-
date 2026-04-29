# Information_monitoring.py

import re
import time
import copy
from typing import Dict, List, Any, Optional, Tuple
from collections import deque


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

    def process_and_clone(self, file_id: str, content: Any) -> Dict[str, Any]:
        """
        1. يدخل الملف الذاكرة المؤقتة.
        2. يخرج معاداً كتابته (نسخة نشطة).
        3. الأصل يبقى مخزناً والنسخة الثانية للعمل.
        """

        # المرحلة 1: الإدخال للذاكرة المؤقتة (Secure Ingestion)
        # نقوم بتخزين "بصمة" الأصل لضمان عدم التلاعب به
        self._immutable_vault[file_id] = {
            "original_data": content,
            "timestamp": time.time(),
            "status": "LOCKED"
        }

        # المرحلة 2: إعادة الكتابة (The Typewriter Mechanism)
        # نستخدم deepcopy لضمان انفصال النسخة الثانية تماماً عن الأصل في الذاكرة
        cloned_version = copy.deepcopy(content)

        # إضافة وسوم "الآلية الكاتبة" (Metadata for the Active Copy)
        active_copy = {
            "data": cloned_version,
            "metadata": {
                "source_id": file_id,
                "version": "2.0_ACTIVE",
                "cloned_at": time.time()
            }
        }

        # المرحلة 3: التوزيع (Dual-State Management)
        # النسخة الثانية تذهب لميدان العمل
        self.active_workspace[file_id] = active_copy

        print(f"✅ [CLONER]: الأصل أؤمن في الخزنة. النسخة النشطة جاهزة للاستخدام.")

        # نرسل النسخة الثانية فقط للاستخدام
        return self.active_workspace[file_id]

    def get_original(self, file_id: str) -> Optional[Any]:
        """استدعاء الأصل من الخزنة عند الحاجة للمقارنة"""
        return self._immutable_vault.get(file_id, {}).get("original_data")

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

    def sense_and_encode(self, raw_input: str, sensory_schema: str) -> Dict[str, Any]:
        """
        تحويل المدخلات الخام إلى كود حسي (Perceptual Code)
        """
        # 1. المرحلة الحسية: استخراج "الترددات" (الكلمات المفتاحية والأنماط)
        frequency_signature = self._extract_frequency_signature(raw_input)

        # 2. التغذية الراجعة من الذاكرة السياقية (Contextual Feedback)
        # هنا يتم تعديل "شدة الإدراك" بناءً على ما تم رؤيته سابقاً
        perception_intensity = self._calculate_resonance(frequency_signature)

        # 3. الترميز الإدراكي (The Perceptual Encoding)
        # لا نخزن النص، بل نخزن "كود إدراكي" يجمع بين المعلومة وشدة حضورها
        perceptual_code = {
            "signature": frequency_signature,
            "intensity": perception_intensity,
            "schema_tag": sensory_schema,
            "timestamp": np.datetime64('now')
        }

        # تغذية الذاكرة السياقية فوراً لرفع الوعي اللحظي
        self.contextual_memory.append(perceptual_code)

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
